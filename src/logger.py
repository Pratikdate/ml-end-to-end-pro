import logging
import os 
from datetime import datetime



LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
loggs_path=os.path.join(os.getcwd(),'logs',LOG_FILE)
os.makedirs(loggs_path,exist_ok=True)
LOG_fILE_PATH=os.path.join(loggs_path,LOG_FILE)
logging.basicConfig(
    filename=LOG_fILE_PATH,
    format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    level=logging.INFO

)

if __name__ == '__main__':
    logging.info('Logging file Starting')