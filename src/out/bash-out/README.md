# FastAPI Bash client

## Overview

This is a Bash client script for accessing FastAPI service.

The script uses cURL underneath for making all REST calls.

## Usage

```shell
# Make sure the script has executable rights
$ chmod u+x 

# Print the list of operations available on the service
$ ./ -h

# Print the service description
$ ./ --about

# Print detailed information about specific operation
$ ./ <operationId> -h

# Make GET request
./ --host http://<hostname>:<port> --accept xml <operationId> <queryParam1>=<value1> <header_key1>:<header_value2>

# Make GET request using arbitrary curl options (must be passed before <operationId>) to an SSL service using username:password
 -k -sS --tlsv1.2 --host https://<hostname> -u <user>:<password> --accept xml <operationId> <queryParam1>=<value1> <header_key1>:<header_value2>

# Make POST request
$ echo '<body_content>' |  --host <hostname> --content-type json <operationId> -

# Make POST request with simple JSON content, e.g.:
# {
#   "key1": "value1",
#   "key2": "value2",
#   "key3": 23
# }
$ echo '<body_content>' |  --host <hostname> --content-type json <operationId> key1==value1 key2=value2 key3:=23 -

# Make POST request with form data
$  --host <hostname> <operationId> key1:=value1 key2:=value2 key3:=23

# Preview the cURL command without actually executing it
$  --host http://<hostname>:<port> --dry-run <operationid>

```

## Docker image

You can easily create a Docker image containing a preconfigured environment
for using the REST Bash client including working autocompletion and short
welcome message with basic instructions, using the generated Dockerfile:

```shell
docker build -t my-rest-client .
docker run -it my-rest-client
```

By default you will be logged into a Zsh environment which has much more
advanced auto completion, but you can switch to Bash, where basic autocompletion
is also available.

## Shell completion

### Bash

The generated bash-completion script can be either directly loaded to the current Bash session using:

```shell
source .bash-completion
```

Alternatively, the script can be copied to the `/etc/bash-completion.d` (or on OSX with Homebrew to `/usr/local/etc/bash-completion.d`):

```shell
sudo cp .bash-completion /etc/bash-completion.d/
```

#### OS X

On OSX you might need to install bash-completion using Homebrew:

```shell
brew install bash-completion
```

and add the following to the `~/.bashrc`:

```shell
if [ -f $(brew --prefix)/etc/bash_completion ]; then
  . $(brew --prefix)/etc/bash_completion
fi
```

### Zsh

In Zsh, the generated `_` Zsh completion file must be copied to one of the folders under `$FPATH` variable.

## Documentation for API Endpoints

All URIs are relative to **

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CHECKApi* | [**checkApiASSIGNMENTApiV1CheckApiGet**](docs/CHECKApi.md#checkapiassingmentapiv1checkapiget) | **GET** /ASSIGNMENT/api/v1/check-api | Check Api
*CHECKApi* | [**protectedASSIGNMENTApiV1CheckProtectedGet**](docs/CHECKApi.md#protectedassingmentapiv1checkprotectedget) | **GET** /ASSIGNMENT/api/v1/check-protected | Protected
*CHECKORACLEDBCONNECTIONApi* | [**checkOracleDbConnectionASSIGNMENTApiV1CheckOracleDbConnectionGet**](docs/CHECKORACLEDBCONNECTIONApi.md#checkoracledbconnectionassingmentapiv1checkoracledbconnectionget) | **GET** /ASSIGNMENT/api/v1/check-oracle-db-connection | Check Oracle Db Connection
*DEEPLEARNINGApi* | [**loadAndTestModelByIndexASSIGNMENTApiV1LoadAndTestModelByIndexGet**](docs/DEEPLEARNINGApi.md#loadandtestmodelbyindexassingmentapiv1loadandtestmodelbyindexget) | **GET** /ASSIGNMENT/api/v1/load-and-test-model-by-index | Load And Test Model By Index
*DEEPLEARNINGApi* | [**loadAndTestModelASSIGNMENTApiV1LoadAndTestModelGet**](docs/DEEPLEARNINGApi.md#loadandtestmodelassingmentapiv1loadandtestmodelget) | **GET** /ASSIGNMENT/api/v1/load-and-test-model | Load And Test Model
*DEEPLEARNINGApi* | [**testAccuracyForRangeOfDataASSIGNMENTApiV1TestAccuracyForRangeOfDataGet**](docs/DEEPLEARNINGApi.md#testaccuracyforrangeofdataassingmentapiv1testaccuracyforrangeofdataget) | **GET** /ASSIGNMENT/api/v1/test-accuracy-for-range-of-data | Test Accuracy For Range Of Data
*DEEPLEARNINGApi* | [**trainAndSaveModelASSIGNMENTApiV1TrainAndSaveModelGet**](docs/DEEPLEARNINGApi.md#trainandsavemodelassingmentapiv1trainandsavemodelget) | **GET** /ASSIGNMENT/api/v1/train-and-save-model | Train And Save Model
*EXCEPTIONApi* | [**raiseExceptionASSIGNMENTApiV1RaiseExceptionGet**](docs/EXCEPTIONApi.md#raiseexceptionassingmentapiv1raiseexceptionget) | **GET** /ASSIGNMENT/api/v1/raise-exception | Raise Exception
*GETREQUESTFROMMYSELFApi* | [**getRequestFromMyselfASSIGNMENTApiV1GetRequestFromMyselfGet**](docs/GETREQUESTFROMMYSELFApi.md#getrequestfrommyselfassingmentapiv1getrequestfrommyselfget) | **GET** /ASSIGNMENT/api/v1/get-request-from-myself | Get Request From Myself
*SENDREQUESTTOMYSELFApi* | [**sendRequestToMyselfASSIGNMENTApiV1SendRequestToMyselfGet**](docs/SENDREQUESTTOMYSELFApi.md#sendrequesttomyselfassingmentapiv1sendrequesttomyselfget) | **GET** /ASSIGNMENT/api/v1/send-request-to-myself | Send Request To Myself
*UPDATECONFApi* | [**updateConfASSIGNMENTApiV1ImbUpdateConfPost**](docs/UPDATECONFApi.md#updateconfassingmentapiv1imbupdateconfpost) | **POST** /ASSIGNMENT/api/v1/imb/update-conf | Update Conf
*UPDATELOGLEVELApi* | [**updateLogLevelASSIGNMENTApiV1ImbUpdateLogLevelPost**](docs/UPDATELOGLEVELApi.md#updateloglevelassingmentapiv1imbupdateloglevelpost) | **POST** /ASSIGNMENT/api/v1/imb/update-log-level | Update Log Level
*USERSApi* | [**addUserASSIGNMENTApiV1UserAddPost**](docs/USERSApi.md#adduserassingmentapiv1useraddpost) | **POST** /ASSIGNMENT/api/v1/user/add | Add User
*USERSApi* | [**deleteUserASSIGNMENTApiV1UserDeleteIdDelete**](docs/USERSApi.md#deleteuserassingmentapiv1userdeleteiddelete) | **DELETE** /ASSIGNMENT/api/v1/user/delete/{id} | Delete User
*USERSApi* | [**getUserASSIGNMENTApiV1UserGetGet**](docs/USERSApi.md#getuserassingmentapiv1usergetget) | **GET** /ASSIGNMENT/api/v1/user/get | Get User
*USERSApi* | [**loginASSIGNMENTApiV1UsersLoginPost**](docs/USERSApi.md#loginassingmentapiv1usersloginpost) | **POST** /ASSIGNMENT/api/v1/users/login | Login
*USERSApi* | [**refreshASSIGNMENTApiV1UsersRefreshPost**](docs/USERSApi.md#refreshassingmentapiv1usersrefreshpost) | **POST** /ASSIGNMENT/api/v1/users/refresh | Refresh
*USERSApi* | [**updateUserASSIGNMENTApiV1UserUpdateIdPut**](docs/USERSApi.md#updateuserassingmentapiv1userupdateidput) | **PUT** /ASSIGNMENT/api/v1/user/update/{id} | Update User


## Documentation For Models

 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [UpdateConf](docs/UpdateConf.md)
 - [Users](docs/Users.md)
 - [ValidationError](docs/ValidationError.md)
 - [VmResponse](docs/VmResponse.md)
 - [VmResponseBase](docs/VmResponseBase.md)
 - [VmUp](docs/VmUp.md)


## Documentation For Authorization

 All endpoints do not require authorization.

