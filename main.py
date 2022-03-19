from dealData import getEnt, deal, change
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('./iris2.csv')
    son_data_list = []
    son_dict_list = []
    part = df['sepalLength'].unique()
    for item in part:
        son_data_dict = {'node': None, 'feature': None, 'data': None}
        data_M = df[df['sepalLength'].map(lambda x: x == item)]
        data_last = data_M.drop(labels='sepalLength', axis=1)
        son_data_list.append(data_last)
        son_data_dict['node'] = 'sepalLength'
        son_data_dict['feature'] = item
        son_data_dict['data'] = data_last
