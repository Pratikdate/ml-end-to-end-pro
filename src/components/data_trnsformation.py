import sys 
from dataclasses import dataclass
import pandas as pd
import numpy as np
from src.utils import save_object

import os
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler


from src.exception import CustomException
from src.logger import logging


@dataclass
class DataTransformationconfig:
    preprocessor_obj_file_path=os.path.join('artifacts','proprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationconfig()
    def get_data_transformation_object(self):
        try:
            '''
            this fuction responsibel for data transformation'''



            numerical_columns=["writing_score","reading_score"]

            categorical_columns=["gender",
                                 "race_ethenicity",
                                 "parental_lavel_of_education",
                                 "lunch",
                                 "test_preparation_cource"
                                 ]
            
            num_pipeline=Pipeline(
                steps=[
                ("impuetr",SimpleImputer(strategy="impuetr")),
                ("std_scaler",StandardScaler())
                 ]
            )

            cat_pipelien=Pipeline(
                steps=[
                ("impuetr",SimpleImputer(strategy="most_frequency")),
                ("hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler())
                ]
            )
            logging.info("Numerical columns standard scaling completed")
            logging.info("categorical coulumns encoding completed")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipeline",cat_pipelien,categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e: 
            raise CustomException(e,sys)
        


    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("read train and test of data done")

            logging.info("obtaining preprocessor object")


            preprocessor_obj=self.get_data_transformation_object()

            target_column_name='math_score'
            numerical_columns=["writing_score","reading_score"]


            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=train_df.drop(columns=[target_column_name],axis=1)

            target_feature_test_df=test_df[target_column_name]
            
            logging.info(f"Appling preprocessor object on training dataframe and dataframe ")

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)


            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)

            train_arr=np.c_[
                input_feature_train_arr,np.array(target_feature_test_df)
            ]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            logging.info("save preprocessing object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )

            return (
                train_arr ,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path


            )


        except Exception as e:
            raise CustomException(e,sys)