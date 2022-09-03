from typing import List
import pandas as pd
import requests
import json
import time
import yaml
import logging
import argparse
from datetime import datetime
from urllib3.exceptions import InsecureRequestWarning
from random import randint, randrange

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

LOG_FILENAME = 'test_service.log'
LOG_LEVEL = logging.INFO
logFormatter = logging.Formatter(
    "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
rootLogger.setLevel(LOG_LEVEL)
fileHandler = logging.FileHandler(LOG_FILENAME, mode='w')
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


class Handler():
    def __init__(self, configfile: str) -> None:
        self._df = None
        self._config = None
        self._sheet_name = None
        self._chat_room_name = None
        self._load_config(configfile=configfile)

    def _load_config(self, configfile: str):
        with open(configfile, 'r') as file:
            self._config = yaml.safe_load(file)

        mode = self._config['mode']
        if mode not in ['critical', 'noncritical']:
            print(
                f'{bcolors.WARNING}Warning: {mode} mode is not valid -> "critical" used instead.{bcolors.ENDC}')

    def get_config(self):
        return self._config

    def load_data(self, room: str):
        self._sheet_name = self._config['rooms'][room]['sheet_name']
        self._chat_room_name = self._config['rooms'][room]['chat_room_name']
        self._df = pd.read_excel(
            self._config['filepath'], sheet_name=self._sheet_name)

    def get_sleep_time(self) -> float:
        return float(self._config['sleep'])

    def get_solution_rooms(self) -> List:
        rooms = self._config['solution_rooms'].split(',')
        rooms_valid = []
        for room in rooms:
            if room in self._config['rooms']:
                rooms_valid.append(room)
        return rooms_valid

    def get_pass_percentage(self) -> float:
        return float(self._config['pass_percentage'])

    def early_stop(self) -> bool:
        return self._config['early_stop']

    def get_data(self):
        mode = self._config['mode']
        if mode == 'critical':
            return self._get_data_critical()
        elif mode == 'noncritical':
            return self._get_data_noncritical()
        return self._get_data_critical()

    def get_data_count(self) -> int:
        return self.get_data().shape[0]

    def _get_data_critical(self):
        return self._df.loc[self._df['iscritical'] == 1][['question', 'answer-text', 'description']]

    def _get_data_noncritical(self):
        return self._df.loc[self._df['iscritical'] == 0][['question', 'answer-text', 'description']]
    
    # here goes your test related functions
    def check_api(self):
        url = self._config['base_url'] + f"/ASSIGNMENT/api/v1/check-api" 
        TT_PROXY = json.loads('{"http": null, "https": null}')  
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'username': 'lsun',
            'apikey': 'defaultapikey',
            'channel': 'server',
            'X-Request-ID': '6789'
        }
        data = {}
        response = requests.get(url=url, headers=headers, proxies=TT_PROXY, verify=False) 
        return response.json()

    
    def model_prediction(self, index:int): 
        url = self._config['base_url'] + f"/ASSIGNMENT/api/v1/load-and-test-model-by-index?index={index}" 
        TT_PROXY = json.loads('{"http": null, "https": null}')  
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'username': 'lsun',
            'apikey': 'defaultapikey',
            'channel': 'server',
            'X-Request-ID': '6789'
        }
        data = {}
        response = requests.get(url=url, headers=headers, proxies=TT_PROXY, verify=False)  
        return response

    def model_train_test_accuracy(self):
        url = self._config['base_url'] + f"/ASSIGNMENT/api/v1/test-accuracy-for-range-of-data?idx1=0&idx2=15" 
        TT_PROXY = json.loads('{"http": null, "https": null}')  
        headers = {
                'accept': 'application/json',
                'Content-Type': 'application/json',
                'username': 'lsun',
                'apikey': 'defaultapikey',
                'channel': 'server',
                'X-Request-ID': '6789'
            }
        data = {}
        response = requests.get(url=url, headers=headers, proxies=TT_PROXY, verify=False)    
        return response 

    def test_model_prediction_true_positive(self):     
        sample_tp_indexes = [2, 11, 13, 14, 24, 25, 27, 38, 41, 42, 47, 50, 54, 56, 57, 59, 60, 68, 71, 83, 84, 92, 93, 94, 97, 104, 106, 107, 108, 109]
        chosen_image_index = sample_tp_indexes[randint(0, len(sample_tp_indexes) - 1)]
        response = self.model_prediction(chosen_image_index)    
        if response.status_code != 200:
                raise Exception(f'status code: {response.status_code}, detail: {response.text}') 
        return response.json() 

    def test_model_prediction_true_negative(self):    
        sample_tn_indexes = [0, 1, 3, 4, 5, 6, 9, 10, 12, 15, 16, 17, 18, 20, 21, 22, 23, 36, 28, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 43, 44, 45, 46]
        chosen_image_index = sample_tn_indexes[randint(0, len(sample_tn_indexes) - 1)]
        response = self.model_prediction(chosen_image_index)    
        if response.status_code != 200:
                raise Exception(f'status code: {response.status_code}, detail: {response.text}') 
        return response.json() 

    def test_model_prediction_false_positive(self):    
        sample_fp_indexes = [8, 53, 91, 105, 147]
        chosen_image_index = sample_fp_indexes[randint(0, len(sample_fp_indexes) - 1)]
        response = self.model_prediction(chosen_image_index)    
        if response.status_code != 200:
                raise Exception(f'status code: {response.status_code}, detail: {response.text}') 
        return response.json() 

    def test_model_prediction_false_negative(self):    
        sample_fn_indexes = [7, 19, 29, 61, 88, 102, 117, 121, 128, 164, 179, 192, 200]
        chosen_image_index = sample_fn_indexes[randint(0, len(sample_fn_indexes) - 1)]    
        response = self.model_prediction(chosen_image_index)    
        if response.status_code != 200:
                raise Exception(f'status code: {response.status_code}, detail: {response.text}') 
        return response.json() 

    def test_model_train_test_accuracy(self):       
        response = self.model_train_test_accuracy()    
        if response.status_code != 200:
                raise Exception(f'status code: {response.status_code}, detail: {response.text}') 
        return response.json() 

class Test():
    def __init__(self, configfile: str) -> None:
        self.cnt_total = 0
        self.cnt_success = 0
        self.cnt_fail = 0
        self.cnt_error = 0
        self.handler = Handler(configfile=configfile)

    def _should_stop(self) -> bool:
        if self.handler.early_stop() == False:
            return False
        if self.cnt_fail * 1.0 / self.cnt_total > 1 - self.handler.get_pass_percentage():
            return True
        return False

    def run(self):
        self.time_start = datetime.now()
        logging.info(
            f'Test started at {self.time_start} with config: {self.handler.get_config()}') 
        # here goes your test to be run

        # Test no.1
        response_actual = {'Hello': 'ASSIGNMENT', 'version': '0.0.1'}
        response_pred = self.handler.check_api() 
        self.cnt_total += 1
        if response_actual == response_pred:
            self.cnt_success += 1
        else:
            self.cnt_fail += 1
            logging.warning(
                f"FAILURE:\n\tresponse_actual_text: {response_actual}\n\tresponse_pred: {response_pred}")
        if self._should_stop():
            return
        time.sleep(self.handler.get_sleep_time())

        # Test no.2   
        response_actual = ['image was truely belongs to cat, and you predicted as cat']
        response_pred = self.handler.test_model_prediction_true_positive()
        self.cnt_total += 1
        if response_actual == response_pred:
            self.cnt_success += 1
        else:
            self.cnt_fail += 1
            logging.warning(
                f"FAILURE:\n\tresponse_actual_text: {response_actual}\n\tresponse_pred: {response_pred}")
        if self._should_stop():
            return
        time.sleep(self.handler.get_sleep_time())

        # Test no.3
        response_actual = ['image was truely belongs to non-cat, and you predicted as non-cat']
        response_pred = self.handler.test_model_prediction_true_negative()
        self.cnt_total += 1
        if response_actual == response_pred:
            self.cnt_success += 1
        else:
            self.cnt_fail += 1
            logging.warning(
                f"FAILURE:\n\tresponse_actual_text: {response_actual}\n\tresponse_pred: {response_pred}")
        if self._should_stop():
            return
        time.sleep(self.handler.get_sleep_time())

        # Test no.4
        response_actual = ['image was truely belongs to non-cat, but you predicted as cat']
        response_pred = self.handler.test_model_prediction_false_positive()
        self.cnt_total += 1

        if response_actual == response_pred:
            self.cnt_success += 1
        else:
            self.cnt_fail += 1
            logging.warning(
                f"FAILURE:\n\tresponse_actual_text: {response_actual}\n\tresponse_pred: {response_pred}")
        if self._should_stop():
            return
        time.sleep(self.handler.get_sleep_time())

        # Test no.5
        response_actual = ['image was truely belongs to cat, but you predicted as non-cat']
        response_pred = self.handler.test_model_prediction_false_negative()
        self.cnt_total += 1
        if response_actual == response_pred:
            self.cnt_success += 1
        else:
            self.cnt_fail += 1
            logging.warning(
                f"FAILURE:\n\tresponse_actual_text: {response_actual}\n\tresponse_pred: {response_pred}")
        if self._should_stop():
            return
        time.sleep(self.handler.get_sleep_time())

        # Test no.6
        response_pred = self.handler.test_model_train_test_accuracy()
        self.cnt_total += 1
        if response_pred['train accuracy'] > 91 and response_pred['test accuracy'] > 86:
            self.cnt_success += 1
        else:
            self.cnt_fail += 1
            logging.warning(
                f"FAILURE:\n\tresponse_pred: {response_pred}") 
                        
        self._print_result()

    def _print_result(self):
        time_end = datetime.now()
        logging.info(
            f'Test finished at {time_end}. It took {time_end - self.time_start}')
        if self.cnt_total == 0:
            logging.info(f"Error: No tests found!")
            print(f"{bcolors.FAIL}Error: No tests found!{bcolors.ENDC}")
            exit(-1)
        elif self.cnt_fail * 1.0 / self.cnt_total > 1 - self.handler.get_pass_percentage():
            logging.info(
                f"Finished. {self.cnt_fail}/{self.cnt_total} ({round(self.cnt_fail * 100.0 / self.cnt_total, 1)}%) failed.")
            print(
                f"{bcolors.FAIL}Finished. {self.cnt_fail}/{self.cnt_total} ({round(self.cnt_fail * 100.0 / self.cnt_total, 1)}%) failed.{bcolors.ENDC}")
            exit(-1)
        else:
            logging.info(
                f"Successfully finished. {self.cnt_success}/{self.cnt_total} ({round(self.cnt_success * 100.0 / self.cnt_total, 1)}%) passed.")
            print(f"{bcolors.OKGREEN}Successfully finished. {self.cnt_success}/{self.cnt_total} ({round(self.cnt_success * 100.0 / self.cnt_total, 1)}%) passed.{bcolors.ENDC}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--configfile', required=True)
    args = parser.parse_args()
    test = Test(configfile=args.configfile)
    test.run()
