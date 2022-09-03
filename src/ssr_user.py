from ttutils.TTConfigHandler import confighandler
app_data_root = confighandler.get_config("APP_DATA", "/srv/data")
from fastapi import APIRouter, Request, Depends, File, UploadFile, Form
# from api.core import config
from ttutils.TTLogging import tt_logger
from time import sleep
import requests
from typing import List
from sqlalchemy.orm import Session
from api.dbutils import crud
from api.viewmodels import vm_users
from api.core import base
from ttutils.CustomHeadersMiddleware import get_request_id
from api.dbutils.database import engine
import os
from train_test_dl import model, data_preparation, predict
import joblib
from PIL import Image
import numpy as np

from ttutils.TTConfigHandler import confighandler


SERVICE_NAME=confighandler.get_config('SERVICE_NAME', 'ASSIGNMENT')
# TARGET_DEPLOY_TYPE=confighandler.get_config('TARGET_DEPLOY_TYPE', 'dev')

BASE_ASSIGNMENT_SERVER_ADDR = confighandler.get_config("BASE_ASSIGNMENT_SERVER_ADDR", "http://assingmentapi:8000") 

SERVER_LISTEN_IP = confighandler.get_config("SERVER_LISTEN_IP", "0.0.0.0")
SERVER_LISTEN_PORT = confighandler.get_config("SERVER_LISTEN_PORT", 8000)

router = APIRouter()
#####################################################################################################
######################################      TEST REQUESTID     ######################################
#####################################################################################################

@router.get(f"/{SERVICE_NAME}/api/v1/send-request-to-myself", tags=["SEND REQUEST TO MYSELF"])
def send_request_to_myself(p1: str, request: Request):
    # important note: to pass x-request-id to the next server import get_request_id method from 
    # ttutils' middleware and call it and include its return in your request headers
    r = requests.request('GET', f'{BASE_ASSIGNMENT_SERVER_ADDR}/{SERVICE_NAME}/api/v1/get-request-from-myself?p1={p1}', headers={"X-Request-ID": get_request_id()}) 
    return {"From ": "Myself", 'To ': r.text}

@router.get(f"/{SERVICE_NAME}/api/v1/get-request-from-myself", tags=["GET REQUEST FROM MYSELF"])
def get_request_from_myself(p1: str, request: Request):
    tt_logger.info(p1) 
    sleep(0.1)
    return "Myself"

@router.get(f"/{SERVICE_NAME}/api/v1/raise-exception", tags=["EXCEPTION"])
def raise_exception(request: Request):
    try:
        1 / 0
    except ZeroDivisionError:
        tt_logger.opt(exception=True, colors=True).info("Exception logged with debug level:") # exception handling while logging
    sleep(0.1)

#####################################################################################################
######################################           USER          ######################################
#####################################################################################################

@router.get(f"/{SERVICE_NAME}/api/v1/user/get", response_model=List[vm_users.Users], tags=["USERS"])
def get_user(skip: int = 0, limit: int = 1000, db: Session = Depends(base.get_db)):
    auth = crud.get_user(db, skip=skip, limit=limit)
    if auth is not None:
        message = "get users"
        tt_logger.info(message)
        return auth
    message = "users table is empty"
    return vm_users.vm_response_base(status = False, message = message , code = "E101")



@router.post(f"/{SERVICE_NAME}/api/v1/user/add", response_model=vm_users.vm_response_base, tags=["USERS"])
def add_user(username: str= Form(...),                
                firstname: str = Form(""),
                lastname: str = Form(""),
                age: str = Form(...),
                nid: str  = Form(...),                
                db: Session = Depends(base.get_db), file: UploadFile = File(...)): # 
    extension = os.path.splitext(file.filename)[1]
    file.file.seek(0)
    file = file.file.read()

    
    in_file_name_full = base.write_user_uuid_media(get_request_id(), extension = extension)
    with open(in_file_name_full,'wb') as f:
        f.write(file)
    auth = crud.add_user(db, username=username, firstname=firstname, lastname=lastname, age=age, nid = nid, image = in_file_name_full)
    if auth:  
        message = "add new user done"  
        tt_logger.info(message)
        return vm_users.vm_response_base(status = True, message = message , code = "S100", data = vm_users.vm_di_user(username=username, firstname=firstname, lastname=lastname,
                            age=age, nid = nid, image = in_file_name_full))
    message = "failed to add this user"
    tt_logger.info(message)
    return vm_users.vm_response_base(status = False, message = message, code = "E101")    


@router.put(f"/{SERVICE_NAME}/api/v1/user/update/{{id}}", response_model=vm_users.vm_response_base, tags=["USERS"])
def update_user(id, username: str= Form(...),                
                firstname: str = Form(""),
                lastname: str = Form(""),
                age: str = Form(...),
                nid: str  = Form(...),
                db: Session = Depends(base.get_db), file: UploadFile = File(...)):
    extension = os.path.splitext(file.filename)[1]
    file.file.seek(0)
    file = file.file.read()

    
    in_file_name_full = base.write_user_uuid_media(get_request_id(), extension = extension)
    with open(in_file_name_full,'wb') as f:
        f.write(file)
    auth = crud.update_user(db, id=id, username=username, firstname=firstname, lastname=lastname,
                            age=age, nid = nid, image=in_file_name_full)    
    if auth:
        message = "user update done"
        tt_logger.info(message)
        return vm_users.vm_response_base(status = True, message = message, code = "S100")
    message = "failed to update user"
    tt_logger.info(message)
    return vm_users.vm_response_base(status = False, message = message, code = "E101")


@router.delete(f"/{SERVICE_NAME}/api/v1/user/delete/{{id}}", response_model=vm_users.vm_response_base, tags=["USERS"])
def delete_user(id, db: Session = Depends(base.get_db)):
    auth = crud.delete_user(db, id=id)
    if auth:
        message = "user delete done"
        tt_logger.info(message)
        return vm_users.vm_response_base(status = True, message = message, code = "S100")  
    message = "failed to delete user" 
    tt_logger.info(message) 
    return vm_users.vm_response_base(status = False, message = message, code = "E101")

#####################################################################################################
######################################           ORACLE        ######################################
#####################################################################################################

@router.get(f"/{SERVICE_NAME}/api/v1/check-oracle-db-connection", tags=["CHECK ORACLE DB CONNECTION"])
def check_oracle_db_connection():
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM emp') # a LegacyCursorResult to get all query contents use all() method
        rs_list = rs.all()
        tt_logger.info(rs_list)
        return rs_list

#####################################################################################################
######################################       DEEP LEARNING     ######################################
#####################################################################################################

@router.get(f"/{SERVICE_NAME}/api/v1/train-and-save-model", tags=["DEEP LEARNING"])
def train_and_save_model(num_iterations: int = 2000, learning_rate: float = 0.005, print_cost: bool = True):  

    train_set_x, train_set_y, test_set_x, test_set_y, classes = data_preparation()
    trained_model = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations = num_iterations, learning_rate = learning_rate, print_cost = print_cost)
    # Save the model as a pickle in a file
    joblib.dump(trained_model, f'{app_data_root}/servicetests/params.pkl')    
    tt_logger.info("model already is trainded and saved")
    return {"learning_rate" : trained_model['learning_rate'],"num_iterations": trained_model['num_iterations']}

@router.get(f"/{SERVICE_NAME}/api/v1/load-and-test-model", tags=["DEEP LEARNING"])
def load_and_test_model(my_image: str, request: Request):  
    dataset_file = f'{app_data_root}/servicetests/params.pkl'
    fname = f"{app_data_root}/servicetests/images/{my_image}.jpg" 

    if not (os.path.exists(dataset_file) and os.path.exists(fname)):
        return {"message": "dataset or image file is not exist"}
    # Load the model from the file
    loaded_model = joblib.load(dataset_file)    
    tt_logger.info("model already is loaded and test")
    tt_logger.info(f'learning_rate = {loaded_model["learning_rate"]}')
    w = loaded_model["w"]
    b = loaded_model["b"]
    # train_set_x, train_set_y, test_set_x, test_set_y = data_preparation()
    
    image = np.array(Image.open(fname).resize((64,64))).reshape((1, 64*64*3)).T
    image = image/255.
    # tt_logger.info (f"test_set_x = {test_set_x.shape}")
    # X = test_set_x[:,index].reshape((1, 64*64*3)).T
    X = image
    return {"predictions": str(predict(w, b, X)), "learning_rate" : loaded_model['learning_rate'],"num_iterations": loaded_model['num_iterations']}

@router.get(f"/{SERVICE_NAME}/api/v1/load-and-test-model-by-index", tags=["DEEP LEARNING"])
def load_and_test_model_by_index(index: int, request: Request):  
    dataset_file = f'{app_data_root}/servicetests/params.pkl'    

    if not os.path.exists(dataset_file):
        return {"message": "dataset file is not exist"}
    # Load the model from the file
    loaded_model = joblib.load(dataset_file)    
    tt_logger.info("model already is loaded and test")
    tt_logger.info(f'learning_rate = {loaded_model["learning_rate"]}')
    w = loaded_model["w"]
    b = loaded_model["b"]
    train_set_x, train_set_y, test_set_x, test_set_y, classes = data_preparation()  
    Y_prediction_test = int(np.squeeze(predict(w, b, train_set_x[:, [index]])))
    Y_true = np.squeeze(train_set_y[0, index])
    tt_logger.info(f'{Y_prediction_test}, {Y_true}')
    if Y_prediction_test == Y_true:
        return{f"image was truely belongs to {classes[Y_true].decode('utf-8')}, and you predicted as {classes[Y_prediction_test].decode('utf-8')}"}
    else:
        return{f"image was truely belongs to {classes[Y_true].decode('utf-8')}, but you predicted as {classes[Y_prediction_test].decode('utf-8')}"}

@router.get(f"/{SERVICE_NAME}/api/v1/test-accuracy-for-range-of-data", tags=["DEEP LEARNING"])
def test_accuracy_for_range_of_data(idx1: int, idx2: int, request: Request):
    dataset_file = f'{app_data_root}/servicetests/params.pkl'  
    if not os.path.exists(dataset_file):
        return {"message": "dataset or image file is not exist"}    
    # Load the model from the file
    loaded_model = joblib.load(dataset_file)    
    tt_logger.info("model already is loaded and test")
    tt_logger.info(f'learning_rate = {loaded_model["learning_rate"]}')
    w = loaded_model["w"]
    b = loaded_model["b"]
    train_set_x, train_set_y, test_set_x, test_set_y, classes = data_preparation()  
    if idx1 < 0 or idx2 > train_set_x.shape[1] or idx2 - idx1 < 1:
        return {"message" : "given range is not valid"}
    Y_prediction_test = predict(w, b, train_set_x[:, idx1 : idx2])
    Y_test = train_set_y[:, idx1 : idx2]
    Y_prediction_train = predict(w, b, train_set_x)
    Y_train = train_set_y
    return{"test accuracy": 100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100, "train accuracy": 100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100}

    

