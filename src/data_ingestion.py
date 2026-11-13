import  pandas as pd

def load_data():
    data = pd.read_csv("Data/Raw/HR-Employee-Attrition.csv")
    return data

if __name__ == '__main__':
    data = load_data()
    print('\nTop 5 values \n')
    print(data.head(), '\n', '-' *95)
    print('\n Show shapes of the data')
    print(data.shape, '\n', '-' * 95)
    print('\n Columns details')
    print(data.columns, '\n', '-' * 95)
