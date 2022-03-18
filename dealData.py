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


def change(df):
    # 将连续值转化为间断值
    for i in range(df.shape[0]):
        if float(df.loc[i, 'sepalLength']) < 5:
            df.loc[i, 'sepalLength'] = '短'
        elif float(df.loc[i, 'sepalLength']) < 6:
            df.loc[i, 'sepalLength'] = '中'
        else:
            df.loc[i, 'sepalLength'] = '长'

        if float(df.loc[i, 'sepalWidth']) < 3.504:
            df.loc[i, 'sepalWidth'] = '短'
        else:
            df.loc[i, 'sepalWidth'] = '长'

        if float(df.loc[i, 'petalLength']) < 4.375:
            df.loc[i, 'petalLength'] = '短'
        elif float(df.loc[i, 'petalLength']) < 5.375:
            df.loc[i, 'petalLength'] = '中'
        else:
            df.loc[i, 'petalLength'] = '长'

        if float(df.loc[i, 'petalWidth']) < 0.625:
            df.loc[i, 'petalWidth'] = '短'
        else:
            df.loc[i, 'petalWidth'] = '长'
    df.to_csv('./iris2.csv')
