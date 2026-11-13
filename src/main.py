from components.data_ingestion import load_data
from components.data_validation import dataset_check
from components.eda import eda_basic


def main():
    data = load_data()
    dataset_check(data)
    eda_basic(data)





if __name__=='__main__':
    main()
