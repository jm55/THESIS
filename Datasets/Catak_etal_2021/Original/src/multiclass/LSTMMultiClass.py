# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:52:43 2018

@author: user
"""

import pandas as pd
from keras import preprocessing
import os
import datetime
from multiclass.AnalizeRunner import AnalizeRunner

##################################################

prefix = "dataset"

data_path = "C:\\Users\\afy\\PycharmProjects\\AnalizeProject\\deep-learning\Data\\result\\2018-09-19 23_05_12.089157\\filtered\\"
model_path = "C:\\Users\\afy\\PycharmProjects\\AnalizeProject\\multiclass\\result\\"
main_folder_name = model_path + str(datetime.datetime.now()).replace(":", "_") + "\\"

runner = AnalizeRunner()

def read_type_data():
    df = pd.read_csv(data_path + prefix + "_types.zip", delimiter=' ', header=None, compression="zip")
    df[0] = df[0].astype('category')
    cat = df[0].cat
    df[0] = df[0].cat.codes
    y = df[0].values
    return y

def read_call_data():
    df = pd.read_csv(data_path + prefix + "_calls.zip", delimiter=' ', header=None, compression="zip")
    D = df.values
    ds_tmp = D[:, 0].tolist()
    ds = []
    for v in ds_tmp:
        ds.append(v.split(','))

    X = preprocessing.sequence.pad_sequences(ds, maxlen=342)
    print(X.shape)
    return X



os.makedirs(main_folder_name)

print("-------------------basliyor------------")
X = read_call_data()
y = read_type_data()


runner.startAnalize(X, y, main_folder_name)