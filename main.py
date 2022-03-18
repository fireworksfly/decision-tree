from dealData import getEnt, deal, change

if __name__ == '__main__':
    df = deal('./iris.csv')
    change(df)