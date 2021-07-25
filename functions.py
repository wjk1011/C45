import pathlib
import os
from os import path
import multiprocessing
import CB as cb
import numpy as np

def bulk_prediction(data, model):
    predictions = []

    for instance in data:
        attribute = data[0].__dir__()
        attribute = attribute[0:attribute.index('Decision') + 1]
        features = np.array(list(map(lambda x:x.__getattr__(i), instance) for i in attribute))
        prediction = cb.predict(model, features)
        predictions.append(prediction)
    data['Prediction'] = predictions


def initializeFolders():
    import sys
    sys.path.append("..")
    pathlib.Path("outputs").mkdir(parents=True, exist_ok=True)
    pathlib.Path("outputs/data").mkdir(parents=True, exist_ok=True)
    pathlib.Path("outputs/rules").mkdir(parents=True, exist_ok=True)

    # -----------------------------------

    # clear existing rules in outputs/

    outputs_path = os.getcwd() + os.path.sep + "outputs" + os.path.sep

    try:
        if path.exists(outputs_path + "data"):
            for file in os.listdir(outputs_path + "data"):
                os.remove(outputs_path + "data" + os.path.sep + file)

        if path.exists(outputs_path + "rules"):
            for file in os.listdir(outputs_path + "rules"):
                if ".py" in file or ".json" in file or ".txt" in file or ".pkl" in file or ".csv" in file:
                    os.remove(outputs_path + "rules" + os.path.sep + file)
    except Exception as err:
        print("WARNING: ", str(err))


# ------------------------------------

def initializeParams(config):
    enableParallelism = True
    num_cores = int(multiprocessing.cpu_count() / 2)  # allocate half of your total cores

    # num_cores = int((3*multiprocessing.cpu_count())/4) #allocate 3/4 of your total cores
    # num_cores = multiprocessing.cpu_count()

    for key, value in config.items():
        if key == 'enableParallelism':
            enableParallelism = value
        elif key == 'num_cores':
            num_cores = value
    config['enableParallelism'] = enableParallelism
    config['num_cores'] = num_cores


    return config


def createFile(file, content):
    f = open(file, "w")
    f.write(content)


def storeRule(file, content):
    f = open(file, "a+")
    f.writelines(content)
    f.writelines("\n")
