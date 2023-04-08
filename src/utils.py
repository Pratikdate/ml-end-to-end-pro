import sys
import os
import dill
import numpy as np
import pandas as pd

from src.exception import CustomException

def save_object(file_path, object):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'w') as file_obj:
            dill.dumps(object,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
