#aim to read data from anywear such as mongodb 
import os 
import sys 
from src.exception import CustomException
from src.logger import logging 
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass



@dataclass
class DataIngectionConfig:
    train_data_path: str=os.path.join("artifacts","train.csv")
    test_data_path: str=os.path.join("artifacts","test.csv")
    raw_data_path: str=os.path.join("artifacts","raw.csv")



class DataInjection:
    def __init__(self):
        self.ingection_config=DataIngectionConfig()

    def initiate_data_injection(self):
        logging.info("Enter the Data ingection method or component")
        try:
            df=pd.read_csv('jupyter\StudentsPerformance.csv')
            logging.info('read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingection_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingection_config.raw_data_path,index=False,header=True)
            logging.info("Initialise train test split")
            train_set,test_set=train_test_split(self.ingection_config.train_data_path,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingection_config.train_data_path,index=False,header=True)
           
            test_set.to_csv(self.ingection_config.test_data_path,index=False,header=True)
            
            logging.info("Ingection of data is completed")


            return (
                self.ingection_config.train_data_path,
                self.ingection_config.test_data_path,
                self.ingection_config.raw_data_path
                
            )

        
        except Exception as e:

            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataInjection()

    obj.initiate_data_injection()