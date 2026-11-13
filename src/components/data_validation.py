import pandas as pd
from data_ingestion import load_data

def dataset_check(data:pd.DataFrame):
    '''
    Performs basic datacheck
    '''
    print('\n'+'*'*102)
    print('DataSet Overview.center(60)')
    print('\n' + '*' * 102)
    print(f'Shape of dataframe{data.shape}')
    print('\n' + '*' * 102)
    print('columns of dataframe')
    print(data.columns.tolist())
    print('\n' + '*' * 102)
    print('Duplicat in dataframe')
    print(data.duplicated().sum())
    print('\n' + '*' * 102)
    print('Missing values in Dataframe')
    print(data.isna().sum())

def main():
    data = load_data()
    dataset_check(data)

if __name__ =='__main__':
        main()


