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


@pytest.mark.order1
def test_reuest_id(filepath):
    if filepath is None:
        pytest.fail("filepath parameter is not exist")
    confs = read_configs(filepath=filepath)
    URL_SERVICE = confs['URL_SERVICE']
    headers = confs['HEADERS']
    # headers = {
    #     "content-type": "application/json",
    # } 
    for i in range(100):
        p1 = str(randrange(10000, 99999))
        headers["X-Request-ID"] = p1
        url = f"{URL_SERVICE}/ASSIGNMENT/api/v1/send-request-to-myself?p1={p1}"    
        response = requests.request("GET", url, headers=headers)
        print(response.json())
        print(response.headers["x-request-id"], p1)
        assert response.headers["x-request-id"] == p1 , str(response.headers["x-request-id"])
        assert response.status_code == 200, f"{response.status_code}"
        assert response.json() == {'From ': 'Myself', 'To ': '"Myself"'}, f"{response.json()}"
# test_reuest_id()

@pytest.mark.order2
def test_exception(filepath):
    if filepath is None:
        pytest.fail("filepath parameter is not exist")
    confs = read_configs(filepath=filepath)
    print(confs)
    URL_SERVICE = confs['URL_SERVICE']
    headers = confs['HEADERS']
    
    # headers = {
    #     "targetservice": "assingment",
    #     "X-Request-ID": "6789",
    #     "content-type": "application/json"
    # }            
    url = f"{URL_SERVICE}/ASSIGNMENT/api/v1/raise-exception"    
    response = requests.request("GET", url, headers=headers)
    print(response.json())    
    assert True

