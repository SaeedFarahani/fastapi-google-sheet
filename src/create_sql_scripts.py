from subprocess import call, DEVNULL, STDOUT
from alembic.migration import MigrationContext
from alembic.config import Config
from alembic import script
from api.dbutils.database import engine

alembic_cfg = Config('alembic.ini')

def get_current_migration_rev_id(cfg, default_val = None):
    directory = script.ScriptDirectory.from_config(cfg)
    migration_rev = directory.get_current_head()    
    return default_val if migration_rev is None else migration_rev 

def get_db_rev_id(connectable):
    with connectable.begin() as connection:
        context = MigrationContext.configure(connection)
        db_rev = context.get_current_revision()        
        return db_rev

def check_db_and_migration_match(cfg, connectable):
    db_rev, migration_rev = get_db_rev_id(connectable), get_current_migration_rev_id(cfg)
    return db_rev == migration_rev
#############################################################################
########################      USED REPEATEDLY       #########################
#############################################################################
def create_sql_script(rev_id, script_file_name):
    call(f"alembic revision --autogenerate --rev-id={rev_id}", shell=True, stderr=DEVNULL)

    call(f"alembic upgrade {rev_id} >> {script_file_name}", shell=True, stderr=DEVNULL)

def create_upgrade_script(from_rev="base", to_rev="head", script_file_name = "script.txt"):
    # Example: alembic upgrade 3:head --sql
    call(f"alembic upgrade {from_rev}:{to_rev} --sql >> {script_file_name}", shell=True, stderr=DEVNULL)

def create_all_upgrade_script(script_file_name = "all_script.txt"):
    # Example: alembic upgrade base:head --sql
    call(f"alembic upgrade base:head --sql >> {script_file_name}", shell=True, stderr=DEVNULL)

def create_relative_upgrade_script(jump_num:int = 1, script_file_name = "script.txt"):
    # Example: alembic upgrade +2 --sql
    call(f"alembic upgrade +{jump_num} --sql >> {script_file_name}", shell=True, stderr=DEVNULL)
def get_info():
    call(f"alembic history --verbose", shell=True, stderr=DEVNULL)
def get_current_revision():
    call(f"alembic current --verbose", shell=True, stderr=DEVNULL)
def get_head():
    call(f"alembic head --verbose", shell=True, stderr=DEVNULL)
#############################################################################

def create_sql_script_auto_incremental_id(script_file_name = 'script.txt'):
    migration_rev_id = get_current_migration_rev_id(alembic_cfg, 1)
    try:
        migration_rev_id = int(migration_rev_id)
    except ValueError:
        raise Exception('migration revision id is not integer')
    
    create_sql_script(migration_rev_id + 1, script_file_name)

def create_sql_script_auto_incremental_id_and_filename():
    migration_rev_id = get_current_migration_rev_id(alembic_cfg, 1)
    try:
        migration_rev_id = int(migration_rev_id)
    except ValueError:
        raise Exception('migration revision id is not integer')
    
    create_sql_script(migration_rev_id + 1, f"script{migration_rev_id + 1}.txt")

def create_last_upgrade_script(script_file_name = "last_script.txt"):
    migration_rev_id = get_current_migration_rev_id(alembic_cfg, 1)
    try:
        migration_rev_id = int(migration_rev_id)
    except ValueError:
        raise Exception('migration revision id is not integer')
    call(f"alembic upgrade {migration_rev_id - 1}:{migration_rev_id} --sql >> {script_file_name}", shell=True, stderr=DEVNULL)

if __name__ == "__main__":
    create_all_upgrade_script()

