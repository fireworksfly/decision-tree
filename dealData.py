import pandas as pd
import numpy as np


def getEnt(data_pd):
    # 计算熵
    ENT_D = 0.0
    items = data_pd[data_pd.keys()[-1]].value_counts()
    print(type(items))
    for item in items:
        print(item)
        ENT_D += (-np.log2(item / len(data_pd[data_pd.keys()[-1]])) * item / len(data_pd[data_pd.keys()[-1]]))
    return ENT_D


def deal(name):
    headers = ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'class']
    df = pd.read_csv(name)
    head = list(df.iloc[0:0, 0:])
    df.columns = headers
    df.loc[df.shape[0]] = head
    return df
