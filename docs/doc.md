assingment-fastapi-api

---
**Service setup**

## in your local
logs and customer data will be in msdata/assingmentapi/data/logs.logs
app data such as database and models will be in app_data/assingmentapi/database

## in docker container
logs and customer data goes into the /srv/cus_data
app data such as database and models goes into the /srv/app_data

## your .env file should include these
```
VOLUME_DIR_SERVICES=../mservices
VOLUME_DIR_APP_DATA=../app_data
VOLUME_DIR_CUS_DATA=../msdata
CUS_DATA=/srv/cus_data
APP_DATA=/srv/app_data
DB_CON_STRING_ASSIGNMENT=sqlite:////srv/app_data/database/sql_app.db
```
rest of them are as before

## your docker-compose should include these
```
volumes:
    - /etc/localtime:/etc/localtime:ro
    - ${VOLUME_DIR_SERVICES}/authaclapi/project/src:/approot/src
    - ${VOLUME_DIR_APP_DATA}/authaclapi/data:${APP_DATA}
    - ${VOLUME_DIR_CUS_DATA}/authaclapi/data:${CUS_DATA}
environment:
    - APP_ALL_ENV_VARS=SERVICE_NAME,EOAPI,TARGET_DEPLOY_TYPE,DB_CON_STRING_ASSIGNMENT,IP_WHITELIST,IP_BLACKLIST,APP_DATA,CUS_DATA 
    - SERVICE_NAME=ASSIGNMENT      
    - DB_CON_STRING_ASSIGNMENT
```
rest of them are as before

## dc-dev and dc-prod in mservices/assingmentapi/project/solsetup should be like this
```
services:
  assingmentapi:
   environment:
      - APP_ALL_ENV_VARS=SERVICE_NAME,EOAPI,TARGET_DEPLOY_TYPE,DB_CON_STRING_ASSIGNMENT,IP_WHITELIST,IP_BLACKLIST,APP_DATA,CUS_DATA 
      - SERVICE_NAME=ASSIGNMENT      
      - DB_CON_STRING_ASSIGNMENT
      - IP_WHITELIST
      - IP_BLACKLIST
      - Selected_MIDDLEWARES
```
## .envdev and .envprod in artinsol/setupsol/assingment should be like this
```
VOLUME_DIR_SERVICES=../mservices
VOLUME_DIR_APP_DATA=../app_data
VOLUME_DIR_CUS_DATA=../msdata
CUS_DATA=/srv/cus_data
APP_DATA=/srv/app_data
rest of them are as before
```

## to read something from configs in mainapi use following codes at first lines
```
from ttutils.TTConfigHandler import confighandler
confighandler.load_config('path_to/conf_filename.yml')
returned_value = confighandler.get_config("var_name_you_need", "default_value_if_var_not_exists")
```
## example:
```
x = confighandler.get_config("SERVICE_VERSION", "0.0.2")
```
# note: you might need to brought above mentioned codes to the first lines of your python file
