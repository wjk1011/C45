import math
import imp
import uuid
import json
import numpy as np
import copy
import multiprocessing.pool
import pandas as pd
import psutil
import gc
import Preprocess
import functions

# ----------------------------------------

global decision_rules


class NoDaemonProcess(multiprocessing.Process):
    # make 'daemon' attribute always return False
    def _get_daemon(self):
        return False

    def _set_daemon(self, value):
        pass

    daemon = property(_get_daemon, _set_daemon)


class NoDaemonContext(type(multiprocessing.get_context())):
    Process = NoDaemonProcess


class MyPool(multiprocessing.pool.Pool):

    def __init__(self, *args, **kwargs):
        kwargs['context'] = NoDaemonContext()
        super(MyPool, self).__init__(*args, **kwargs)


# ----------------------------------------
def  calculateEntropy(data, attribute, config):
    algorithm = config['algorithm']

    # --------------------------

    instances = len(data)
    columns = len(attribute)
    # print(instances," rows, ",columns," columns")

    decisions = list(set(list(map(lambda x: x.Decision, data))))

    entropy = 0

    for i in decisions:
        num_of_decisions = list(map(lambda x: x.Decision, data)).count(i)
        # print(decision,"->",num_of_decisions)

        class_probability = num_of_decisions / instances

        entropy = entropy - class_probability * math.log(class_probability, 2)
    return entropy


def findDecision(data, attribute, config):
    # information gain for id3, gain ratio for c4.5, gini for cart, chi square for chaid and std for regression
    algorithm = config['algorithm']

    resp_obj, categoricalization_data = findGains(data, attribute, config)
    gains = list(resp_obj["gains"].values())
    entropy = resp_obj["entropy"]

    winner_index = 0
    metric_value = 0
    metric_name = None
    if algorithm == "ID3":
        winner_index = gains.index(max(gains))
        metric_value = entropy
        metric_name = "Entropy"
    elif algorithm == "C4.5":
        winner_index = gains.index(max(gains))
        metric_value = entropy
        metric_name = "Entropy"

    winner_name = attribute[winner_index]
    return winner_name, len(data), metric_value, metric_name, gains, categoricalization_data


def findGains(data, attribute, config):
    algorithm = config['algorithm']
    data = copy.deepcopy(data)
    # -----------------------------
    entropy = 0
    if algorithm == "ID3" or algorithm == "C4.5":
        entropy = calculateEntropy(data, attribute, config)
    columns = len(attribute)
    instances = len(data)
    gains = []

    for i in range(0, columns - 1):
        column_name = attribute[i]
        column_type = type(data[0].__getattribute__(column_name))
        # 이거도 걍 맨 첫 번째 값으로만 타입 확인...........
        # print(column_name,"->",column_type)

        if column_type != str:
            # 대부분 numpy.float 형
            data = Preprocess.processContinuousFeatures(algorithm, data, attribute, column_name, entropy, config)

        classes = set(map(lambda x: x.__getattribute__(column_name), data))

        splitinfo = 0
        if algorithm == 'ID3' or algorithm == 'C4.5':
            gain = entropy
        else:
            gain = 0

        for j in range(0, len(classes)):
            current_class = list(classes)[j]
            # print(column_name,"->",current_class)

            subdataset = list(filter(lambda x:x.__getattribute__(column_name) == current_class, data))
            # print(subdataset)

            subset_instances = len(subdataset)
            class_probability = subset_instances / instances

            if algorithm == 'ID3' or algorithm == 'C4.5':
                subset_entropy = calculateEntropy(subdataset, attribute, config)
                gain = gain - class_probability * subset_entropy

            if algorithm == 'C4.5':
                splitinfo = splitinfo - class_probability * math.log(class_probability, 2)

        # iterating over classes for loop end
        # -------------------------------

        if algorithm == 'C4.5':
            if splitinfo == 0:
                splitinfo = 100  # this can be if data set consists of 2 rows and current column consists of 1 class. still decision can be made (decisions for these 2 rows same). set splitinfo to very large value to make gain ratio very small. in this way, we won't find this column as the most dominant one.
            gain = gain / splitinfo

        # ----------------------------------

        gains.append(gain)

    # -------------------------------------------------

    resp_obj = {}
    resp_obj["gains"] = {}

    for idx, feature in enumerate(attribute[0:-1]):  # Decision is always the last column
        # print(idx, feature)
        resp_obj["gains"][feature] = gains[idx]

    resp_obj["entropy"] = entropy

    return resp_obj, data


def createBranchWrapper(func, args):
    return func(*args)


def createBranch(config, current_class, subdataset, numericColumn, branch_index
                 , winner_name, winner_index, root, parents, file, dataset_features, num_of_instances, metric, gains,
                 tree_id=0, main_process_id=None):

    custom_rules = []
    algorithm = config['algorithm']
    enableParallelism = config['enableParallelism']

    charForResp = "'"
    if algorithm == 'Regression':
        charForResp = ""
    # ---------------------------
    tmp_root = root * 1
    parents_raw = copy.copy(parents)
    # ---------------------------

    if numericColumn == True:
        compareTo = current_class  # current class might be <=x or >x in this case
    else:
        compareTo = " == '" + str(current_class) + "'"

    terminateBuilding = False

    # -----------------------------------------------
    # can decision be made?
    attribute = subdataset[0].__dir__()
    attribute = attribute[0:attribute.index('Decision') + 1]
    final_decision = None
    if len(set(map(lambda x:x.Decision, subdataset))) == 1:
        final_decision = list(map(lambda x:x.Decision, subdataset))[0]  # all items are equal in this case
        terminateBuilding = True

    elif len(attribute) == 1:  # if decision cannot be made even though all columns dropped
        final_decision_list = list(set((i.Decision for i in subdataset)))
        final_decision = final_decision_list[[final_decision_list.count(i)
                                              for i in final_decision_list].index(max([final_decision_list.count(i)
                                                                                       for i in final_decision_list]))] # get the most frequent one
        terminateBuilding = True
    # -----------------------------------------------

    if enableParallelism == True:
        check_condition = "if"  # TODO: elif checks might be above than if statements in parallel
    else:
        if branch_index == 0:
            check_condition = "if"
        else:
            check_condition = "elif"

    check_rule = check_condition + " obj[" + str(winner_index) + "]" + compareTo + ":"

    leaf_id = str(uuid.uuid1())

    if enableParallelism != True:
        functions.storeRule(file, (functions.formatRule(root), "", check_rule))
    else:
        sample_rule = {}
        sample_rule["current_level"] = root
        sample_rule["leaf_id"] = leaf_id
        sample_rule["parents"] = parents
        sample_rule["rule"] = check_rule
        sample_rule["feature_idx"] = winner_index
        sample_rule["feature_name"] = winner_name
        sample_rule["instances"] = num_of_instances
        sample_rule["metric"] = metric
        sample_rule["return_statement"] = 0
        sample_rule["tree_id"] = tree_id

        # json to string
        sample_rule = json.dumps(sample_rule)

        custom_rules.append(sample_rule)

    # -----------------------------------------------

    if terminateBuilding == True:  # check decision is made

        parents = copy.copy(leaf_id)
        leaf_id = str(uuid.uuid1())

        decision_rule = "return " + charForResp + str(final_decision) + charForResp

        if enableParallelism != True:
            # serial
            functions.storeRule(file, (functions.formatRule(root + 1), decision_rule))
        else:
            # parallel
            sample_rule = {}
            sample_rule["current_level"] = root + 1
            sample_rule["leaf_id"] = leaf_id
            sample_rule["parents"] = parents
            sample_rule["rule"] = decision_rule
            sample_rule["feature_idx"] = winner_index
            sample_rule["feature_name"] = winner_name
            sample_rule["instances"] = num_of_instances
            sample_rule["metric"] = 0
            sample_rule["return_statement"] = 1
            sample_rule["tree_id"] = tree_id

            # json to string
            sample_rule = json.dumps(sample_rule)

            custom_rules.append(sample_rule)

    else:  # decision is not made, continue to create branch and leafs
        root = root + 1  # the following rule will be included by this rule. increase root
        parents = copy.copy(leaf_id)


        # --------------------------------------------------------
        attribute = subdataset[0].__dir__()
        attribute = attribute[0:attribute.index('Decision') + 1]
        #---------------------------------------------------------
        results = buildDecisionTree(subdataset, attribute, root, file, config, dataset_features
                                    , root - 1, leaf_id, parents, tree_id=tree_id, main_process_id=main_process_id)

        custom_rules = custom_rules + results

        root = tmp_root * 1
        parents = copy.copy(parents_raw)

    gc.collect()

    return custom_rules


def buildDecisionTree(data, attribute, root, file, config, dataset_features, parent_level=0, leaf_id=0, parents='root', tree_id=0,
                      validation_df=None, main_process_id=None):

    models = []

    decision_rules = []

    feature_names = attribute

    enableParallelism = config['enableParallelism']

    json_file = file.split(".")[0] + ".json"

    # --------------------------------------

    data_copy = copy.deepcopy(data)

    winner_name, num_of_instances, metric, metric_name, gains, categoricalization_data = findDecision(data, attribute, config)

    # find winner index, this cannot be returned by find decision because columns dropped in previous steps
    j = 0
    winner_index = 0
    for i in dataset_features:
        if i == winner_name:
            winner_index = j
        j = j + 1

    numericColumn = False
    if dataset_features[winner_name] != str:
        numericColumn = True

    # restoration
    columns = len(attribute)
    for i in range(0, columns - 1):
        # column_name = df.columns[i]; column_type = df[column_name].dtypes #numeric field already transformed to object. you cannot check it with df itself, you should check df_copy
        column_name = attribute[i]
        # 이거도 걍 맨 첫 번째 값으로만 타입 확인...........
        column_type = type(data[0].__getattribute__(attribute[i]))
        if column_type != str and column_name != winner_name:
            for j in range(len(data)):
                setattr(data[j], column_name, data_copy[j])
    classes = list(set(map(lambda x:x.__getattribute__(winner_name), categoricalization_data)))
    # print("classes: ",classes," in ", winner_name)
    # -----------------------------------------------------

    num_cores = config["num_cores"]

    input_params = []

    # serial approach
    subdataset = []
    for i in range(0, len(classes)):
        current_class = classes[i]
        subdataset = list(filter(lambda x:x.__getattribute__(winner_name) == current_class if hasattr(x, winner_name) is True else None, categoricalization_data))
        for j in subdataset:
            delattr(j, winner_name)
        branch_index = i

        # create branches serially

        if enableParallelism is True:
            input_params.append((config, current_class, subdataset, numericColumn, branch_index
                                 , winner_name, winner_index, root, parents, file, dataset_features, num_of_instances,
                                 metric, tree_id, main_process_id))

    # ---------------------------
    # add else condition in the decision tree


    # 이거도 첫 번째 값만 타입 확인,,,,,,,,,,,,,,,,,,,,,
    if type(list(map(lambda x:x.Decision, data))[0]) == str:  # classification
        data = [list(set(map(lambda x:x.Decision, subdataset))),[]]
        for i in data[0]:
            data[1].append(len(list(filter(lambda x:x.Decision == i, subdataset))))

        else_decision = "return '%s'" % (data[0][0])

        if enableParallelism != True:
            functions.storeRule(file, (functions.formatRule(root), "else:"))
            functions.storeRule(file, (functions.formatRule(root + 1), else_decision))
        else:  # parallelism
            leaf_id = str(uuid.uuid1())

            check_rule = "else: " + else_decision

            sample_rule = {}
            sample_rule["current_level"] = root
            sample_rule["leaf_id"] = leaf_id
            sample_rule["parents"] = parents
            sample_rule["rule"] = check_rule
            sample_rule["feature_idx"] = -1
            sample_rule["feature_name"] = ""
            sample_rule["instances"] = len(data)
            sample_rule["metric"] = 0
            sample_rule["return_statement"] = 0
            sample_rule["tree_id"] = tree_id

            # json to string
            sample_rule = json.dumps(sample_rule)
            decision_rules.append(sample_rule)


    # ---------------------------

    try:
        main_process = psutil.Process(main_process_id)
        children = main_process.children(recursive=True)
        active_processes = len(children) + 1  # plus parent
    # active_processes = len(children)
    except:
        active_processes = 100  # set a large initial value

    results = []
    # create branches in parallel
    if enableParallelism == True:

        if parent_level == 0:
            # if main_process_id != None and num_cores >= active_processes + len(classes): #len(classes) branches will be run in parallel #this causes hang and deadlock

            # --------------------------------
            """
            #causes hang problem if number of input_params is greater than num_cores
            pool = MyPool(num_cores)
            branch_results = pool.starmap(createBranch, input_params)
            
            for branch_result in branch_results:
                for leaf_result in branch_result:
                    results.append(leaf_result)
            
            pool.close()
            pool.join()
            pool.terminate()
            
            gc.collect()
            """
            # --------------------------------

            # workaround for hang problem. set num_cores and active threads same.
            # len(classes) == len(input_params)
            # e.g. len(input_params) = 5, num_cores = 2, cycles = 3
            # we will feed 2 items to pool in for loops instead of 5

            cycles = int(len(input_params) / num_cores) + 1

            for i in range(0, cycles):

                filter_begin = i * num_cores
                filter_end = i * num_cores + num_cores

                if filter_end > len(input_params):
                    filter_end = filter_end

                input_frame = input_params[filter_begin: filter_end]

                pool = MyPool(num_cores)
                branch_results = pool.starmap(createBranch, input_frame)

                pool.close()
                pool.join()
                pool.terminate()
                gc.collect()

                for branch_result in branch_results:
                    for leaf_result in branch_result:
                        results.append(leaf_result)

        # --------------------------------

        else:
            for input_param in input_params:
                sub_results = createBranchWrapper(createBranch, input_param)
                for sub_result in sub_results:
                    results.append(sub_result)

        # --------------------------------

        decision_rules = decision_rules + results

        # --------------------------------

        if root != 1:  # return children results until the root node
            return decision_rules

    # ---------------------------------------------

    if root == 1:

        if enableParallelism == True:

            # custom rules are stored in decision_rules. merge them all in a json file first

            json_rules = "[\n"  # initialize

            file_index = 0
            for custom_rule in decision_rules:

                json_rules += custom_rule

                if file_index < len(decision_rules) - 1:
                    json_rules += ", "

                json_rules += "\n"

                file_index = file_index + 1

            # -----------------------------------

            json_rules += "]"
            functions.createFile(json_file, json_rules)

            # -----------------------------------
            # reconstruct rules from json to py

            reconstructRules(json_file, feature_names)

        # -----------------------------------

        # is regular decision tree

        moduleName = "outputs/rules/rules"
        fp, pathname, description = imp.find_module(moduleName)
        myrules = imp.load_module(moduleName, fp, pathname, description)  # rules0
        models.append(myrules)

    return models


def findPrediction(row):
    params = []
    num_of_features = row.shape[0] - 1
    for j in range(0, num_of_features):
        params.append(row[j])

    moduleName = "outputs/rules/rules"
    fp, pathname, description = imp.find_module(moduleName)
    myrules = imp.load_module(moduleName, fp, pathname, description)  # rules0

    prediction = myrules.findDecision(params)
    return prediction


"""
If you set parelellisim True, then branches will be created parallel. Rules are stored in a json file randomly. This program reconstructs built rules in a tree form. In this way, we can build decision trees faster.
"""


def reconstructRules(source, feature_names, tree_id=0):
    # print("Reconstructing ",source)

    file_name = source.split(".json")[0]
    file_name = file_name + ".py"

    # -----------------------------------

    constructor = "def findDecision(obj): #"
    idx = 0
    for feature in feature_names:
        constructor = constructor + "obj[" + str(idx) + "]: " + feature

        if idx < len(feature_names) - 1:
            constructor = constructor + ", "
        idx = idx + 1

    functions.createFile(file_name, constructor + "\n")

    # -----------------------------------

    with open(source, 'r') as f:
        rules = json.load(f)

    # print(rules)

    def padleft(rule, level):
        for i in range(0, level):
            rule = "\t" + rule
        return rule

    # print("def findDecision(obj):")

    max_level = 0

    rule_set = []
    # json file might not store rules respectively
    for instance in rules:
        if len(instance) > 0:
            rule = []
            rule.append(instance["current_level"])
            rule.append(instance["leaf_id"])
            rule.append(instance["parents"])
            rule.append(instance["rule"])
            rule.append(instance["feature_name"])
            rule.append(instance["instances"])
            rule.append(instance["metric"])
            rule.append(instance["return_statement"])
            rule_set.append(rule)
        # print(padleft(instance["rule"], instance["current_level"]))

    df = np.array(rule_set)

    def extractRules(df, parent='root', level=1):

        level_raw = level * 1
        parent_raw = copy.copy(parent)

        else_rule = ""

        leaf_idx = 0
        for i in range(0, df.shape[0]):
            current_level = int(df[i][0])
            leaf_id = df[i][1]
            parent_id = df[i][2]
            rule = df[i][3]
            feature_name = df[i][4]
            instances = int(df[i][5])
            metric = float(df[i][6])
            return_statement = int(df[i][7])

            if parent_id == parent:

                if_statement = False
                if rule[0:2] == "if":
                    if_statement = True

                else_statement = False
                if rule[0:5] == "else:":
                    else_statement = True
                    else_rule = rule

                # ------------------------

                if else_statement != True:

                    if if_statement == True and leaf_idx > 0:
                        rule = "el" + rule

                    # print(padleft(rule, level), "(", leaf_idx,")")

                    if leaf_idx == 0 and return_statement == 0:
                        explainer = {}
                        explainer["feature"] = feature_name
                        explainer["instances"] = instances
                        explainer["metric_value"] = round(metric, 4)
                        explainer["depth"] = current_level
                        explainer = "# " + json.dumps(explainer)
                        functions.storeRule(file_name, padleft(explainer, level))

                    functions.storeRule(file_name, padleft(rule, level))

                    level = level + 1;
                    parent = copy.copy(leaf_id)
                    extractRules(df, parent, level)
                    level = level_raw * 1;
                    parent = copy.copy(parent_raw)  # restore

                    leaf_idx = leaf_idx + 1

        # add else statement

        if else_rule != "":
            # print(padleft(else_rule, level))
            functions.storeRule(file_name, padleft(else_rule, level))

    # ------------------------------------

    extractRules(df)

# ------------------------------------
