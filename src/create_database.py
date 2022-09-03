import os
from ttutils.TTConfigHandler import confighandler

conf_dir = os.environ.get("CONF_DATA", "../conf")
conf_filename = os.path.join(conf_dir, 'app-conf.yml')
confighandler.load_config(conf_filename)

print(f'conf_dir : {conf_dir}')
print(f'conf_filename : {conf_filename}')

from alembic import config, command
from alembic.migration import MigrationContext
from alembic.config import Config
from sqlalchemy import create_engine
from api.dbutils.database import engine
from loguru import logger
from api.dbutils.models import Base
from api.dbutils import models
from alembic import script
from alembic.runtime import migration
from datetime import datetime

alembic_cfg = Config('alembic.ini')

rev_id = datetime.now().strftime("%Y%m%d%H%M%S")

alembic_cfg = Config('alembic.ini')

def check_current_head(cfg, connectable):
    directory = script.ScriptDirectory.from_config(cfg)
    with connectable.begin() as connection:
        context = MigrationContext.configure(connection)
        db_rev = context.get_current_revision()
        migration_rev = directory.get_current_head()
        return db_rev, migration_rev

db_rev, migration_rev = check_current_head(alembic_cfg, engine)
print("1: ", db_rev, migration_rev)

if db_rev is None:
    if migration_rev is None:
        print("db rev is none and migration rev is empty")        
        command.revision(alembic_cfg, autogenerate=True, rev_id=rev_id)
        db_rev, migration_rev = check_current_head(alembic_cfg, engine)
        print("3: ", db_rev, migration_rev)
        # command.stamp(alembic_cfg, 'head') # creates table only for alembic_version
        command.upgrade(alembic_cfg, 'head') # creates table for model and alembic_version        
        db_rev, migration_rev = check_current_head(alembic_cfg, engine)
        print("4: ", db_rev, migration_rev)
    else:
        print("db rev is none but migration rev is non-empty")
        command.stamp(alembic_cfg, 'head')
        command.upgrade(alembic_cfg, 'head') # creates table for model and alembic_version        
        db_rev, migration_rev = check_current_head(alembic_cfg, engine)
        print("2: ", db_rev, migration_rev)
else: 
    if migration_rev is None:
        print("db rev is not-none but migration rev is empty") # That's trouble
        command.stamp(alembic_cfg, 'base', purge=True)
        command.revision(alembic_cfg, autogenerate=True)
        db_rev, migration_rev = check_current_head(alembic_cfg, engine)
        print("3: ", db_rev, migration_rev)        
        # command.stamp(alembic_cfg, 'head') # creates table only for alembic_version
        command.upgrade(alembic_cfg, 'head') # creates table for model and alembic_version
        db_rev, migration_rev = check_current_head(alembic_cfg, engine)
        print("5: ", db_rev, migration_rev)
    else:
        print("db rev is not-none and migration rev is non-empty")
        if db_rev == migration_rev:
            print("db rev and migration rev match") # Evrything is ok
        else:
            print("db rev and migration rev does not match") # That's trouble
            command.stamp(alembic_cfg, 'head', purge=True)
            command.upgrade(alembic_cfg, 'head') # creates table for model and alembic_version        
            db_rev, migration_rev = check_current_head(alembic_cfg, engine)
            print("6: ", db_rev, migration_rev)