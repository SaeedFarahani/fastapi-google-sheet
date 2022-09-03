from ttutils.TTConfigHandler import confighandler

from sqlalchemy.orm import Session
from api.dbutils import models
import datetime
from datetime import datetime, timedelta
from api.core import utils
from sqlalchemy import literal, or_
from ttutils.TTLogging import tt_logger

def get_valid_channels():
    valid_channels = [
        'MOBILE',
        'VTM',
        'ATM',
        'SERVER',
        'PC',
        'ANDROID',
        'IOS',
        'WEB'
    ]
    return valid_channels

ADMIN_USERNAME = confighandler.get_config("ADMIN_USERNAME", "ttaiadmin")
ADMIN_PASSWORD = confighandler.get_config("ADMIN_PASSWORD", "Techno@1996$*")

#####################################################################
# USERS
#####################################################################


def is_user_valid(username: str, password: str):
    password = utils.matching_number(password)
    if username != ADMIN_USERNAME or utils.check_password(password, utils.get_hashed_password(ADMIN_PASSWORD)) != True:
        return False
    return True


def get_user(db: Session, skip: int = 0, limit: int = 1000):
    tt_logger.info("get_user in crud called")
    return db.query(models.Users).offset(skip).limit(limit).all()


def add_user(db: Session, username: str, firstname: str, lastname: str, age: str, nid: str, image: str = ""):
    item = models.Users(username=username, firstname=firstname, lastname=lastname, age = age, nid = nid, image=image)
    tt_logger.info("add_user in crud called")
    try:
        db.add(item)
        db.commit()
        return True
    except:
        return False


def update_user(db: Session, id: int, username: str, firstname: str, lastname: str, age: str, nid: str, image: str = ""):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if user is not None:
        if username:
            user.username = username
        if firstname:
            user.firstname = firstname
        if lastname:
            user.lastname = lastname
        if age:
            user.age = age
        if nid:
            user.nid = nid
        if image:
            user.image = image
        try:
            tt_logger.info("update_user in crud called")
            db.commit()
            return True
        except:
            tt_logger.info('Failed to update')
            return False
    else:
        tt_logger.info("User not found")
        return False


def delete_user(db: Session, id: int):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if user is not None:
        try:
            db.delete(user)
            db.commit()
            tt_logger.info("delete_user in crud called")
            return True
        except:
            tt_logger.info('Failed to delete')
            return False
    else:
        tt_logger.info("User not found")
        return False
