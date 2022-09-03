import os

from sqlalchemy.orm import Session
from api.dbutils import crud
from api.dbutils.database import SessionLocal
# from api.core import config
from api.core import utils

import datetime

from ttutils.TTConfigHandler import confighandler
CUS_DATA = confighandler.get_config("CUS_DATA", "/srv/cus_data")
SAVE_INCOMING_DIR = os.path.join(CUS_DATA, 'save', 'in')
SAVE_OUTGOING_DIR = os.path.join(CUS_DATA, 'save', 'out')
# models.Base.metadata.create_all(bind=engine)

INPUT_FRAME_SIZE = (640, 480)

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class BASE():
    def __init__(self):
        pass

    def initialization(self):
        # make essential directories
        # meke dataset dir if not exist
        # if not os.path.exists(config.database_dir):
        #     os.makedirs(config.database_dir)

        # meke pics dir if not exist
        # if not os.path.exists(config.log_dir):
        #     os.makedirs(config.log_dir)  
        pass        

    # def generate_apikey(self):
    #     apikey = utils.generate_guid(config.GUID_SIZE)
    #     return apikey

    #####################################################################
    # Check-IP-WhiteList
    #####################################################################
    def check_client_ip_access_whitelist(self, whitelistiprule, clientip):
        return crud.check_client_ip_access(whitelistiprule, clientip)

#####################################################################
# Methods to save upload files
#####################################################################
def get_or_create_input_uudir(uuid: str, dirname: str, dtstr: str):
    inudir = os.path.join(SAVE_INCOMING_DIR, dirname, f"{dtstr}_{uuid}")
    if not os.path.exists(inudir):
        os.makedirs(inudir)
    return inudir
    
def write_user_uuid_media(uuid: str, extension: str):
    now = datetime.datetime.now()
    dirname = f"{now.year:04d}{now.month:02d}{now.day:02d}" # returns directory named with current date including leading zeros
    dtstr = now.strftime("%Y-%m-%d_%H-%M-%S")
    inuudir = get_or_create_input_uudir(uuid=uuid, dtstr=dtstr, dirname=dirname)    
    img_path = os.path.join(inuudir, f"{uuid}{extension}")
    return img_path


  
