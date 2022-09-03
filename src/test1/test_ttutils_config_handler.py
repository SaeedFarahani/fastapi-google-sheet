import os
import pytest
from ttutils.TTConfigHandler import confighandler

# conf_dir = os.environ.get("CONF_DATA", "../conf")
conf_filename = 'test_confs_file.yml'
confighandler.load_config(conf_filename)
######################################################
# Test how to get env vars using ttutils confighandler
######################################################
def get_env_var_before_set():
    # we should get default values before we set env vars
    print("we should get default values before we set env vars")
    ENV_STR_VAR = confighandler.get_config('ENV_STR_VAR', "STR_DEFAULT")
    ENV_INT_VAR = confighandler.get_config('ENV_INT_VAR', 456)
    ENV_BOOL_VAR = confighandler.get_config('ENV_BOOL_VAR', False)
    ENV_FLOAT_VAR = confighandler.get_config('ENV_FLOAT_VAR', 3.4)

    print(ENV_STR_VAR, type(ENV_STR_VAR))
    print(str(ENV_INT_VAR), type(ENV_INT_VAR))
    print(str(ENV_BOOL_VAR), type(ENV_BOOL_VAR))
    print(str(ENV_FLOAT_VAR), type(ENV_FLOAT_VAR))
    return ENV_STR_VAR, ENV_INT_VAR, ENV_BOOL_VAR, ENV_FLOAT_VAR

def set_envs():
# Set environment variables
    os.environ['ENV_STR_VAR'] = "Test_ENV_STR"
    os.environ['ENV_INT_VAR'] = "123"
    os.environ['ENV_BOOL_VAR'] = "True"
    os.environ['ENV_FLOAT_VAR'] = "1.2"

    # Get environment variables
    ENV_STR_VAR = os.environ.get('ENV_STR_VAR')
    ENV_INT_VAR = os.environ.get('ENV_INT_VAR')
    ENV_BOOL_VAR = os.environ.get('ENV_BOOL_VAR')
    ENV_FLOAT_VAR = os.environ.get('ENV_FLOAT_VAR')
    print("we set following varialbes in env")
    print(ENV_STR_VAR)
    print(ENV_INT_VAR)
    print(ENV_BOOL_VAR)
    print(ENV_FLOAT_VAR)
    return ENV_STR_VAR, ENV_INT_VAR, ENV_BOOL_VAR, ENV_FLOAT_VAR

def env_vars_after_set():    
    confighandler.load_config(conf_filename)
    # now we should get what we set
    print("now we should get what we set")
    ENV_STR_VAR = confighandler.get_config('ENV_STR_VAR', "STR_DEFAULT")
    ENV_INT_VAR = confighandler.get_config('ENV_INT_VAR', 456)
    ENV_BOOL_VAR = confighandler.get_config('ENV_BOOL_VAR', True)
    ENV_FLOAT_VAR = confighandler.get_config('ENV_FLOAT_VAR', 3.4)

    print(ENV_STR_VAR, type(ENV_STR_VAR))
    print(str(ENV_INT_VAR), type(ENV_INT_VAR))
    print(str(ENV_BOOL_VAR), type(ENV_BOOL_VAR))
    print(str(ENV_FLOAT_VAR), type(ENV_FLOAT_VAR))

    return ENV_STR_VAR, ENV_INT_VAR, ENV_BOOL_VAR, ENV_FLOAT_VAR

def get_conf_file_vars():
    print("and we get following variables from config files")
    FILE_STR_VAR = confighandler.get_config('FILE_STR_VAR', "STR_DEFAULT")
    FILE_INT_VAR = confighandler.get_config('FILE_INT_VAR', 456)
    FILE_BOOL_VAR = confighandler.get_config('FILE_BOOL_VAR', True)
    FILE_FLOAT_VAR = confighandler.get_config('FILE_FLOAT_VAR', 3.4)

    print(FILE_STR_VAR, type(FILE_STR_VAR))
    print(str(FILE_INT_VAR), type(FILE_INT_VAR))
    print(str(FILE_BOOL_VAR), type(FILE_BOOL_VAR))
    print(str(FILE_FLOAT_VAR), type(FILE_FLOAT_VAR))

    return FILE_STR_VAR, FILE_INT_VAR, FILE_BOOL_VAR, FILE_FLOAT_VAR

@pytest.mark.order1
def test_env_var_before_set():
    ENV_STR_VAR, ENV_INT_VAR, ENV_BOOL_VAR, ENV_FLOAT_VAR = get_env_var_before_set()
    assert [ENV_STR_VAR, ENV_INT_VAR, ENV_BOOL_VAR, ENV_FLOAT_VAR] == ['STR_DEFAULT', 456, False, 3.4]
    assert [type(ENV_STR_VAR), type(ENV_INT_VAR), type(ENV_BOOL_VAR), type(ENV_FLOAT_VAR)] == [type(""), type(0), type(True), type(1.2)]

@pytest.mark.order2
def test_set_envs():
    ENV_STR_VAR, ENV_INT_VAR, ENV_BOOL_VAR, ENV_FLOAT_VAR = set_envs()
    assert [ENV_STR_VAR, ENV_INT_VAR, ENV_BOOL_VAR, ENV_FLOAT_VAR] == ['Test_ENV_STR', '123', 'True', '1.2']

@pytest.mark.order3
def test_env_vars_after_set():
    ENV_STR_VAR, ENV_INT_VAR, ENV_BOOL_VAR, ENV_FLOAT_VAR = env_vars_after_set()
    assert [ENV_STR_VAR, ENV_INT_VAR, ENV_BOOL_VAR, ENV_FLOAT_VAR] == ['Test_ENV_STR', 123, 'True', 1.2]
    assert [type(ENV_STR_VAR), type(ENV_INT_VAR), type(ENV_BOOL_VAR), type(ENV_FLOAT_VAR)] == [type(""), type(0), type('True'), type(1.2)]
######################################################
# Test how to get env vars using ttutils confighandler
######################################################
@pytest.mark.order4
def test_conf_file_vars():
    FILE_STR_VAR, FILE_INT_VAR, FILE_BOOL_VAR, FILE_FLOAT_VAR = get_conf_file_vars()
    assert [FILE_STR_VAR, FILE_INT_VAR, FILE_BOOL_VAR, FILE_FLOAT_VAR] == ['Test_FILE_STR', 789, True, 5.6]
    assert [type(FILE_STR_VAR), type(FILE_INT_VAR), type(FILE_BOOL_VAR), type(FILE_FLOAT_VAR)] == [type(""), type(0), type(True), type(1.2)]

if __name__=="__main__":
    test_env_var_before_set()
    test_set_envs()
    test_env_vars_after_set()
    test_conf_file_vars()