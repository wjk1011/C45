import math
import numpy as np
import data_load
import copy
import time


def buildDecisionTree(data, attribute, config, start=True, max_depth=3):
    origin_data = copy.deepcopy(data)  # returnToOriginData 을 위해 원형 데이터 보존 필요
    winner_attribute = findGains(data, attribute, config)  # branch 에 쓰일 attribute 선택 / instance 에서 연속형 변수들 범주형으로 변함
    classes = list(set(map(lambda x: x.__getattribute__(winner_attribute.name), data)))

    # =========================================

    leaf_list = []  # 모든 leaf
    result_leaf = []  # terminateBuilding 이 True 인 leaf
    start_time = time.time()
    if start:

        # =========================================

        for _leaf, _index in enumerate(range(len(classes))):
            _leaf = data_load.Leaf()
            if winner_attribute.type is 'Continuous':
                _leaf.rule += 'obj.' + str(winner_attribute.name) + ' ' + str(classes[_index])
            if winner_attribute.type is 'Categorical':
                _leaf.rule += 'obj.' + str(winner_attribute.name) + ' is ' + "'" + str(classes[_index]) + "'"
            processed_data = list(filter(lambda x: x.__getattribute__(winner_attribute.name) == classes[_index], data))

            # =========================================

            returnToOriginData(processed_data, origin_data)  # instance 에서 연속형 변수들이 범주형으로 변한 걸 원상태로 되돌림

            # =========================================

            _leaf.dataset = processed_data  # parent leaf 의 데이터 에서 child leaf 로 branch 된 데이터만 가져감

            # =========================================

            if winner_attribute.type is 'Categorical':  # 이번 branch 에 쓰인 attribute 가 범주형이면 그 attribute 는 삭제
                for i in _leaf.dataset:
                    i.usedCategorical.append(winner_attribute.name)
                    delattr(i, winner_attribute.name)

            # =========================================
            # branch 중지 조건
            if len(set(map(lambda x: x.Decision, _leaf.dataset))) == 1:
                _leaf.terminateBuilding = True
                result_leaf.append(_leaf)  # branch 중지 시, result_leaf 에 넣어야 함

            # =========================================
            _leaf.branch += 1
            leaf_list.append(_leaf)  # 모든 leaf 는 leaf_list 에 들어감

        start = False

    # =========================================

    origin_data2 = copy.deepcopy(origin_data)  # copy 가 헷갈려서 line 62 에서 처럼 copy 를 반복하고 있음
    while len(set(filter(lambda x: x.terminateBuilding is False, leaf_list))) >= 1:
        for _leaf in list(filter(lambda x: x.terminateBuilding is False, leaf_list)):  # 이제부터 _leaf 는 parent leaf 로 생각하면 됩니다.

            # =========================================

            origin_data = copy.deepcopy(origin_data2)
            returnToOriginData(_leaf.dataset, origin_data)

            # =========================================

            winner_attribute = findGains(_leaf.dataset, attribute, config)
            classes = list(set(map(lambda x: x.__getattribute__(winner_attribute.name), _leaf.dataset)))

            # =========================================

            for _child_leaf, _index in enumerate(range(len(classes))):
                _child_leaf = data_load.Leaf()
                _child_leaf.branch = _leaf.branch + 1
                _child_leaf.rule = _leaf.rule + ' and '  # parent leaf 의 rule 을 그대로 이어 적기 위해 가져옴
                if winner_attribute.type is 'Continuous':
                    _child_leaf.rule += 'obj.' + str(winner_attribute.name)  + str(classes[_index])
                if winner_attribute.type is 'Categorical':
                    _child_leaf.rule += 'obj.' + str(winner_attribute.name) + ' is ' + "'" + str(classes[_index]) + "'"
                processed_data = list(
                    filter(lambda x: x.__getattribute__(winner_attribute.name) == classes[_index], _leaf.dataset))

                # =========================================

                #returnToOriginData(processed_data, origin_data)

                # =========================================

                _child_leaf.dataset = processed_data
                for i in _child_leaf.dataset:
                    _leaf.dataset.remove(i)

                # =========================================

                if winner_attribute.type is 'Categorical':
                    for i in _child_leaf.dataset:
                        i.usedCategorical.append(winner_attribute.name)
                        delattr(i, winner_attribute.name)

                # =========================================
                # branch 중지 조건
                if not _child_leaf.terminateBuilding:
                    # 1. dataset 의 Decision 종류가 1개일 경우
                    if len(set(map(lambda x: x.Decision, _child_leaf.dataset))) == 1:
                        _child_leaf.terminateBuilding = True
                        result_leaf.append(_child_leaf)

                    # 2. max depth = 3
                    if _child_leaf.branch >= max_depth:
                        _child_leaf.terminateBuilding = True
                        result_leaf.append(_child_leaf)

                    # 3.

                    # 4.

                    # 5.

                # =========================================

                leaf_list.append(_child_leaf)
            _leaf.terminateBuilding = True  # branch 를 마친 parent leaf 는 branch 중지 해야함

            # =========================================
    return result_leaf

def returnToOriginData(processed_data, origin_data):
    id_list = [i.id for i in processed_data]
    for i in range(len(id_list)):
        processed_data[i] = list(filter(lambda x: x.id == id_list[i], origin_data))[0]



def findGains(data, attribute, config):
    gains = []
    algorithm = config['algorithm']
    entropy = calculateEntropy(data, config)
    attribute = list(filter(lambda x: x.name not in data[0].usedCategorical, attribute))
    for _index in range(len(attribute) - 1):
        if attribute[_index].type is 'Continuous':
            data = processContinuousFeatures(data, attribute[_index], entropy, config)

        # =========================================

        #if attribute[_index].type is 'Categorical':
        #    if attribute[_index].name not in data[0].usedCategorical:
        #        classes = set(map(lambda x:x.__getattribute__(attribute[_index].name), data))

        classes = set(map(lambda x: x.__getattribute__(attribute[_index].name), data))

        # =========================================

        splitinfo = 0
        if algorithm == 'ID3' or algorithm == 'C4.5':
            gain = entropy
        else:
            gain = 0

        for j in range(0, len(classes)):
            current_class = list(classes)[j]

            subdataset = list(filter(lambda x: x.__getattribute__(attribute[_index].name) == current_class, data))

            subset_instances = len(subdataset)
            class_probability = subset_instances / len(data)

            if algorithm == 'ID3' or algorithm == 'C4.5':
                subset_entropy = calculateEntropy(subdataset, config)
                gain = gain - class_probability * subset_entropy

            if algorithm == 'C4.5':
                splitinfo = splitinfo - class_probability * math.log(class_probability, 2)

        if algorithm == 'C4.5':
            if splitinfo == 0:
                splitinfo = 100  # this can be if data set consists of 2 rows and current column consists of 1 class. still decision can be made (decisions for these 2 rows same). set splitinfo to very large value to make gain ratio very small. in this way, we won't find this column as the most dominant one.
            gain = gain / splitinfo

        gains.append(gain)
    winner_index = 0
    if algorithm == "ID3":
        winner_index = gains.index(max(gains))
    elif algorithm == "C4.5":
        winner_index = gains.index(max(gains))

    winner_attribute = attribute[winner_index]
    return winner_attribute



def calculateEntropy(data, config):
    instances = len(data)
    decisions = list(set(list(map(lambda x: x.Decision, data))))
    entropy = 0
    for i in decisions:
        num_of_decisions = list(map(lambda x: x.Decision, data)).count(i)
        class_probability = num_of_decisions / instances
        entropy = entropy - class_probability * math.log(class_probability, 2)
    return entropy


def processContinuousFeatures(data, attribute, entropy, config):
    algorithm = config['algorithm']
    if len(set(map(lambda x: x.__getattribute__(attribute.name), data))) <= 20:
        unique_values = np.array(sorted(set(map(lambda x: x.__getattribute__(attribute.name), data))))

    else:
        unique_values = []
        data_min = np.array(list(map(lambda x: x.__getattribute__(attribute.name), data))).min()
        data_max = np.array(list(map(lambda x: x.__getattribute__(attribute.name), data))).max()
        scales = list(range(7))
        for scale in scales:
            unique_values.append(data_min + ((data_max - data_min) / (len(scales) - 1) * scale))

    subset_gainratios = []
    subset_gains = []

    if len(unique_values) == 1:
        winner_threshold = unique_values[0]
        for i in data:
            if i.__getattribute__(attribute.name) <= winner_threshold:
                setattr(i, attribute.name, "<=" + str(winner_threshold))
            else:
                setattr(i, attribute.name, ">" + str(winner_threshold))
        return data

    for i in range(0, len(unique_values) - 1):
        threshold = unique_values[i]
        subset1 = list(filter(lambda x: x.__getattribute__(attribute.name) <= threshold, data))
        subset2 = list(filter(lambda x: x.__getattribute__(attribute.name) > threshold, data))

        subset1_rows = len(subset1)
        subset2_rows = len(subset2)
        total_instances = len(data)

        subset1_probability = subset1_rows / total_instances
        subset2_probability = subset2_rows / total_instances

        threshold_gain = 0
        if algorithm == 'ID3' or algorithm == 'C4.5':
            threshold_gain = entropy - subset1_probability * calculateEntropy(subset1,
                                                                              config) - subset2_probability * calculateEntropy(
                subset2, config)
            subset_gains.append(threshold_gain)
        if algorithm == 'C4.5':  # C4.5 also need gain in the block above. That's why, instead of else if we used direct if condition here
            threshold_splitinfo = -subset1_probability * math.log(subset1_probability,
                                                                  2) - subset2_probability * math.log(
                subset2_probability, 2)
            gainratio = threshold_gain / threshold_splitinfo
            if gainratio is None:
                print(1)
            subset_gainratios.append(gainratio)
    winner_one = 0
    if algorithm == "C4.5":
        if len(subset_gainratios) == 0:
            print(1)
        winner_one = subset_gainratios.index(max(subset_gainratios))
    elif algorithm == "ID3":  # actually, ID3 does not support for continuous features but we can still do it
        winner_one = subset_gains.index(max(subset_gains))

    winner_threshold = unique_values[winner_one]
    for i in data:
        if i.__getattribute__(attribute.name) <= winner_threshold:
            setattr(i, attribute.name, "<=" + str(winner_threshold))
        else:
            setattr(i, attribute.name, ">" + str(winner_threshold))

    return data
