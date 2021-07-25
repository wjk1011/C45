import numpy as np
import math
import Training


def processContinuousFeatures(algorithm, df, attribute, column_name, entropy, config):
    # if True:
    if len(set(map(lambda x: x.__getattribute__(column_name), df))) <= 20:  # 칼럼별 고유값의 개수
        unique_values = np.array(sorted(set(map(lambda x: x.__getattribute__(column_name), df))))
    else:
        unique_values = []
        df_mean = np.array(list(map(lambda x: x.__getattribute__(column_name), df))).mean()
        df_std = np.array(list(map(lambda x: x.__getattribute__(column_name), df))).std(ddof=0)
        df_min = np.array(list(map(lambda x: x.__getattribute__(column_name), df))).min()
        df_max = np.array(list(map(lambda x: x.__getattribute__(column_name), df))).max()
        unique_values.append(df_min)
        unique_values.append(df_max)
        unique_values.append(df_mean)
        scales = list(range(-3, +4, 1))
        for scale in scales:
            if df_min < df_mean + scale * df_std < df_max:
                unique_values.append(df_mean + scale * df_std)
        unique_values.sort()
    # print(column_name,"->",unique_values)
    subset_gainratios = []
    subset_gains = []
    subset_ginis = []
    subset_red_stdevs = []
    subset_chi_squares = []

    if len(unique_values) == 1:
        winner_threshold = unique_values[0]
        for i in df:
            if i.__getattribute__(column_name) <= winner_threshold:
                setattr(i, column_name, "<=" + str(winner_threshold))
            else:
                setattr(i, column_name, ">" + str(winner_threshold))
        return df

    # ------------------------------------
    for i in range(0, len(unique_values) - 1):
        threshold = unique_values[i]
        subset1 = list(filter(lambda x: x.__getattribute__(column_name) <= threshold, df))
        subset2 = list(filter(lambda x: x.__getattribute__(column_name) > threshold, df))

        subset1_rows = len(subset1)
        subset2_rows = len(subset2)
        total_instances = len(df)  # subset1_rows+subset2_rows

        subset1_probability = subset1_rows / total_instances
        subset2_probability = subset2_rows / total_instances

        if algorithm == 'ID3' or algorithm == 'C4.5':
            threshold_gain = entropy - subset1_probability * Training.calculateEntropy(subset1, attribute,
                                                                                       config) - subset2_probability * Training.calculateEntropy(
                subset2, attribute, config)
            subset_gains.append(threshold_gain)

        if algorithm == 'C4.5':  # C4.5 also need gain in the block above. That's why, instead of else if we used direct if condition here

            threshold_splitinfo = -subset1_probability * math.log(subset1_probability,
                                                                  2) - subset2_probability * math.log(
                subset2_probability, 2)
            gainratio = threshold_gain / threshold_splitinfo
            subset_gainratios.append(gainratio)

        # ----------------------------------

        # 회귀는 다음에 합시다...
        """
        elif algorithm == 'Regression':
            superset_stdev = df['Decision'].std(ddof=0)
            subset1_stdev = subset1['Decision'].std(ddof=0)
            subset2_stdev = subset2['Decision'].std(ddof=0)

            threshold_weighted_stdev = (subset1_rows / total_instances) * subset1_stdev + (
                        subset2_rows / total_instances) * subset2_stdev
            threshold_reducted_stdev = superset_stdev - threshold_weighted_stdev
            subset_red_stdevs.append(threshold_reducted_stdev)
        """
    # ----------------------------------

    if algorithm == "C4.5":
        winner_one = subset_gainratios.index(max(subset_gainratios))
    elif algorithm == "ID3":  # actually, ID3 does not support for continuous features but we can still do it
        winner_one = subset_gains.index(max(subset_gains))
    elif algorithm == "Regression":
        winner_one = subset_red_stdevs.index(max(subset_red_stdevs))

    winner_threshold = unique_values[winner_one]
    # print(column_name,": ", winner_threshold," in ", unique_values)

    # print("theshold is ",winner_threshold," for ",column_name)
    for i in df:
        if i.__getattribute__(column_name) <= winner_threshold:
            setattr(i, column_name, "<=" + str(winner_threshold))
        else:
            setattr(i, column_name, ">" + str(winner_threshold))

    return df
