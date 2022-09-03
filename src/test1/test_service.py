import requests
import time
import os
import pytest
from datetime import datetime

from random import randint, randrange
import yaml

def read_configs(filepath) -> None:   
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
                return yaml.load(f, Loader=yaml.FullLoader)

global test_user_id
global test_group_id

expected_response_false = False
expected_response_true = True
# headers = {
#         "content-type": "application/json",
#     } 
# URL_SERVICE='http://0.0.0.0:6198'  # to send request to the assingment directly use 6103 port 

def model_prediction(URL_SERVICE:str, headers, index:int):
    
    
    url = f"{URL_SERVICE}/ASSIGNMENT/api/v1/load-and-test-model-by-index?index={index}"    
    response = requests.request("GET", url, headers=headers)    
    print(response.json(), str(index))    
    return response  

def model_train_test_accuracy(URL_SERVICE:str, headers):
    url = f"{URL_SERVICE}/ASSIGNMENT/api/v1/test-accuracy-for-range-of-data?idx1=0&idx2=15"    
    response = requests.request("GET", url, headers=headers)    
    print(response.json())
    return response 

@pytest.mark.order1
def test_model_prediction_true_positive(filepath):
    if filepath is None:
        pytest.fail("filepath parameter is not exist")
    confs = read_configs(filepath=filepath)
    print(confs)
    URL_SERVICE = confs['URL_SERVICE']
    headers = confs['HEADERS']
    sample_tp_indexes = [2, 11, 13, 14, 24, 25, 27, 38, 41, 42, 47, 50, 54, 56, 57, 59, 60, 68, 71, 83, 84, 92, 93, 94, 97, 104, 106, 107, 108, 109]
    chosen_image_index = sample_tp_indexes[randint(0, len(sample_tp_indexes) - 1)]
    response = model_prediction(URL_SERVICE, headers, chosen_image_index)    
    assert response.status_code == 200, f"{response.status_code}"
    assert response.json() == ['image was truely belongs to cat, and you predicted as cat']

@pytest.mark.order2
def test_model_prediction_true_negative(filepath):
    if filepath is None:
        pytest.fail("filepath parameter is not exist")
    confs = read_configs(filepath=filepath)
    print(confs)
    URL_SERVICE = confs['URL_SERVICE']
    headers = confs['HEADERS']
    sample_tn_indexes = [0, 1, 3, 4, 5, 6, 9, 10, 12, 15, 16, 17, 18, 20, 21, 22, 23, 36, 28, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 43, 44, 45, 46]
    chosen_image_index = sample_tn_indexes[randint(0, len(sample_tn_indexes) - 1)]
    response = model_prediction(URL_SERVICE, headers, chosen_image_index)    
    assert response.status_code == 200, f"{response.status_code}"
    assert response.json() == ['image was truely belongs to non-cat, and you predicted as non-cat']

@pytest.mark.order3
def test_model_prediction_false_positive(filepath):
    if filepath is None:
        pytest.fail("filepath parameter is not exist")
    confs = read_configs(filepath=filepath)
    print(confs)
    URL_SERVICE = confs['URL_SERVICE']
    headers = confs['HEADERS']
    sample_fp_indexes = [8, 53, 91, 105, 147]
    chosen_image_index = sample_fp_indexes[randint(0, len(sample_fp_indexes) - 1)]
    response = model_prediction(URL_SERVICE, headers, chosen_image_index)    
    assert response.status_code == 200, f"{response.status_code}"
    assert response.json() == ['image was truely belongs to non-cat, but you predicted as cat']

@pytest.mark.order4
def test_model_prediction_false_negative(filepath):
    if filepath is None:
        pytest.fail("filepath parameter is not exist")
    confs = read_configs(filepath=filepath)
    print(confs)
    URL_SERVICE = confs['URL_SERVICE']
    headers = confs['HEADERS']
    sample_fn_indexes = [7, 19, 29, 61, 88, 102, 117, 121, 128, 164, 179, 192, 200]
    chosen_image_index = sample_fn_indexes[randint(0, len(sample_fn_indexes) - 1)]    
    response = model_prediction(URL_SERVICE, headers, chosen_image_index)    
    assert response.status_code == 200, f"{response.status_code}"
    assert response.json() == ['image was truely belongs to cat, but you predicted as non-cat']

@pytest.mark.order5
def test_model_train_test_accuracy(filepath): 
    if filepath is None:
        pytest.fail("filepath parameter is not exist")
    confs = read_configs(filepath=filepath)
    print(confs)    
    URL_SERVICE = confs['URL_SERVICE']    
    headers = confs['HEADERS']   
    response = model_train_test_accuracy(URL_SERVICE, headers)    
    assert response.status_code == 200, f"{response.status_code}"
    assert response.json()['train accuracy'] > 91
    assert response.json()['test accuracy'] > 86

if __name__ == "__main__":
    for index in range(10):
        model_prediction(index)
    test_model_train_test_accuracy()