
from components.data_ingestion import load_data
from components.data_validation import dataset_check
from components.eda import eda_basic
from components.visualization import save_charts

def main():
    data = load_data()
    dataset_check(data)
    eda_basic(data)
    save_charts(data)





if __name__=='__main__':
    main()
