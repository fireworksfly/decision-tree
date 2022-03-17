from dealData import getEnt, deal
if __name__ == '__main__':
    df = deal('./iris.csv')
    part = df['sepalLength'].unique()
    print(part)
