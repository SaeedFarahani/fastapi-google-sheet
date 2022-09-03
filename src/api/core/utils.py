import random
import string
import os
import re
from unidecode import unidecode
import bcrypt

# defining function for random
# string id with parameter


def generate_guid(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def get_config(env, val):
    envval = os.environ.get(env)
    if (envval is None or envval == ""):
        return val
    else:
        if type(val) == type(0):        # int type
            return int(envval)
        elif type(val) == type(0.1):    # float type
            return float(envval)
    return envval


def generate_otp():
    return random.randint(100000, 999999)


def verify_cellnum(cellnum):
    rgxpattern = "^(\+98|0|0098)?(9\d{9})$"
    result = re.match(rgxpattern, cellnum)
    if result is not None:
        cellnum = cellnum[-10:]
        return True, cellnum
    else:
        return False, None


def is_cellnum(username: str):
    username = matching_number(username)
    is_cellnum, _ = verify_cellnum(username)
    return is_cellnum


def matching_number(number):
    # Use it only for numbers
    return unidecode(number)


def is_username_valid(username: str):
    rgxpattern = "[a-zA-Z0-9_@\\.]{6,128}"
    # rgxpattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!#%*?&]{6,20}$"  # number, uppercase, lowercase
    # rgxpattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"  # number, uppercase, lowercase, special symbol
    result = re.match(rgxpattern, username)
    if result is not None:
        return True
    else:
        return False


# Nowhere used!
def is_password_valid(password: str):
    # number, uppercase, lowercase
    rgxpattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!#%*?&]{6,20}$"
    # rgxpattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"  # number, uppercase, lowercase, special symbol
    result = re.match(rgxpattern, password)
    if result is not None:
        return True
    else:
        return False


def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())


def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)
