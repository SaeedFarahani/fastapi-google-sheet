# Example execution command:
# run in provision directory:
# DB_CON_STRING_AUTHACL="sqlite:///../base_authacl_api/data/database/sql_app.db" python3 migrate_plain_passwords.py


import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], '..'))
from api.dbutils import models
from api.core import utils
from api.core import base


db = next(base.get_db())
users = db.query(models.Users).all()
if users is not None and len(users) > 0:
    for user in users:
        if isinstance(user.password, bytes):
            password = user.password.decode('utf-8')
        else:
            password = user.password
        if password.startswith('$2b$12$'):
            continue
        hashed_password = utils.get_hashed_password(password)
        user.password = hashed_password
        try:
            db.commit()
            print(user.username, 'password updated')
        except:
            print('Failed to update', user.username)
else:
    print("Users not found or empty")
