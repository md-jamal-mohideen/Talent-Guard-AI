import pandas as pd

from data_ingestion import load_data

if __name__=='__main__':
    data = load_data()
    print(data.head())
    print(data.shape)
    print(data.columns)