from api.core import utils
import sys
import os
from ttutils.TTConfigHandler import confighandler
sys.path.insert(0, os.pardir)
# from data.config import current_dir as data_dir


# SERVICE_NAME=confighandler.get_config('SERVICE_NAME', 'ASSIGNMENT')
# TARGET_DEPLOY_TYPE=confighandler.get_config('TARGET_DEPLOY_TYPE', 'dev')
# CUS_DATA = confighandler.get_config("CUS_DATA", "/srv/cus_data")
# SAVE_INCOMING_DIR = os.path.join(CUS_DATA, 'save', 'in')
# SAVE_OUTGOING_DIR = os.path.join(CUS_DATA, 'save', 'out')
# database_dir = os.path.join(CUS_DATA, 'database/')
# DB_CON_STRING = confighandler.get_config("DB_CON_STRING_ASSIGNMENT", "")
# log_dir = os.path.join(CUS_DATA, 'logs/')

# BASE_ASSIGNMENT_SERVER_ADDR = confighandler.get_config("BASE_ASSIGNMENT_SERVER_ADDR", "http://assingmentapi:8000") 

# SERVER_LISTEN_IP = confighandler.get_config("SERVER_LISTEN_IP", "0.0.0.0")
# SERVER_LISTEN_PORT = confighandler.get_config("SERVER_LISTEN_PORT", 8000)