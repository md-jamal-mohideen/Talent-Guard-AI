import pandas as pd

from data_ingestion import load_data


def eda_basic(data:pd.DataFrame):
    print('\n'+'*'*102)
    print("\nExploratory Data Analysis.center(60)")
    print('='*120)
    print(f'Shapes of the data{data.shape}')
    print('\n'+'*'*102)
    print('\nTarget Variable distribution\n')
    print(data['Attrition'].value_counts())
    print('\n' + '*' * 102)
    print('\nDepartment variable distribution\n')
    print(data['Department'].value_counts())
    print('\n' + '*' * 102)
    print('\n Numerical variable distribution\n')
    print(data.describe())
    print('\n' + '*' * 102)
    print(pd.crosstab(data['OverTime'],data['Attrition']))


def main():

    data = load_data()
    eda_basic(data)


if __name__=='__main__':
    main()