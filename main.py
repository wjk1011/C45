import pandas as pd
import CB as cb

# ----------------------------------------------

parallelism_cases = [True]


class Dataization(object):
    def __init__(self, keys, values):
        for (key, value) in zip(keys, values):
            self.__dict__[key] = value


if __name__ == '__main__':

    for enableParallelism in parallelism_cases:
        print("-------------------------")
        print("Validation set case")
        df = pd.read_csv("dataset/wine.csv")
        train_data, test_data = cb.data_split(df, 0.3)

        # ---------------------------
        # class and pandas to numpy
        attribute = [i.replace(' ','') for i in df]
        train_data_value = train_data.to_numpy()
        test_data_value = test_data.to_numpy()
        train_data = [Dataization(attribute, df.iloc[i]) for i in range(train_data_value.shape[0])]
        test_data = [Dataization(attribute, df.iloc[i]) for i in range(test_data_value.shape[0])]
        # --------------------------

        config = {'algorithm': 'C4.5', 'enableParallelism': enableParallelism}

        model = cb.fit(train_data, config, attribute, target_label='Decision', validation_df=test_data)

    print("-------------------------")
    print("unit tests completed successfully...")
