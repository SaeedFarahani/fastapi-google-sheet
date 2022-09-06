### within mainapi.py at end lines but before if __name__ == "__main__" put following codes to create yaml file from swagger docs within mainapi.py 
```
import yaml
if 'TARGET_DEPLOY_TYPE' in os.environ and os.environ['TARGET_DEPLOY_TYPE'] == 'dev':
    with open('swagger_docs.yml', 'w') as outfile:
        yaml.dump(app.openapi(), outfile, default_flow_style=False)
```
-----------------------------------------------------------------------
### use yaml file created from previous step and run following command where yaml file is located to create client.sh file
```
docker run --rm --user $(id -u):$(id -g) -v ${PWD}:$HOME/local openapitools/openapi-generator-cli generate -i $HOME/local/swagger_docs.yml -g bash -o $HOME/local/test  
```
-----------------------------------------------------------------------
### go to the location of client.sh file you specified at previous step by -o flag and run following commands, you must change host, port, operations and parameters based on your own service
### get help
```
bash client.sh --help
```
### check api
```
bash client.sh checkApiASSIGNMENTApiV1CheckApiGet --host localhost:6103
```
### add a user
```
bash client.sh --host localhost:6103 -F 'username=test1' -F 'firstname=test1' -F 'lastname=test1' -F 'age=34' -F 'nid=123' -F 'file=@sajjad.jpeg'addUserASSIGNMENTApiV1UserAddPost
```
### get user
```
bash client.sh --host localhost:6103 getUserASSIGNMENTApiV1UserGetGet skip=0 limit=1000
```
### edit user
```
bash client.sh --host localhost:6103 -F 'username=test1_edited' -F 'firstname=test1' -F 'lastname=test1' -F 'age=34' -F 'nid=123' -F 'file=@sajjad.jpeg'updateUserASSIGNMENTApiV1UserUpdateIdPut id=1
```
### delete user
```
bash client.sh --host localhost:6103 deleteUserASSIGNMENTApiV1UserDeleteIdDelete id=1
```

To facilitate running bunch of tests with a single “ make test” command where our Makefile is located, we decided to put all test related commands and parameters into an excel file.

In order to do this task, Artinsol is responsible to use prepare.py script in initialization phase to fetch test related files from somewhere, and looks in each service for test directory, which includes test_service_config_template.yml, test_service.py and requirements.txt files, in test phase.
test_service.py reads test_service_config.yml file and gets some parameters to use for tests, such as, sheets, host, root_dir, filepath and mode.
1. sheets: sheets tells which sheets of excel file must be ran, for example, repo-checkapi.
2. host: host tells where test requests must be sent, for example, localhost:8008.
3. root_dir: root_dir is where our test related files located.
4. filepath: filepath is test file name or file path.
5. bash_script_path: bash_script_path is bash file path we may run within our tests.
6. mode : mode is whether critical or noncritical, based on this mode we test those tests with is_critical set as 1 for critical and as 0 for noncritical in excel file.

Excel columns: 
operation, parameters,	headers, request_body, file, iscritical, command, descriptions, desired_response, parameters_to_get_from_response

operation: operation determines which endpoint of service api we are going to test, for example, checkApiQNAGWApiV1CheckApiGet which is for chechapi endpoint of QNA GW service.


Parameters: parameters are variables and their values we are going to send alongside the request, for example, skip=0 limit=1000.

Headers: headers are some key values we are going to send alongside the request, for example, apikey:defaultapikey username:lsun channel:server.

request_body: request_body is json format key values we are going to send alongside the request, for example, ROOM_ID==test_room_id CST_ROL_ID==test-rol-id.

file: file is file object we are going to send alongside the request, for example, -F ‘file=@image.jpeg’

iscritical:  iscritical tells this test is critical if it’s value is 1 else is non-critical.

Command: command is bash command. Sometimes we may need to run bash commands between our tests such as, echo hello this is a test.

Descriptions: descriptions are some descriptions about current test not required but just for guiding one who is running the test.

Desired_response: is what we expected to see in test request’s response. To check whether a test is passed or not we need to compare the true response with desired response.

parameter_to_get_from_response: sometimes we need to get a value of a parameter from previous request’s response to use for next test request, for example, face_id. Next request must include that parameter with $$$ prefix such as: -F 'face_id=$$$face_id'.


So step-by-step guide:
1. add these lines to the mainapi.py
```
import yaml
if 'TARGET_DEPLOY_TYPE' in os.environ and os.environ['TARGET_DEPLOY_TYPE'] == 'dev':
with open('swagger_docs.yml', 'w') as outfile:
yaml.dump(app.openapi(), outfile, default_flow_style=False)
```

2. run mainapi.py to create swagger_docs.yml
3. run this command to create client.sh within src/test directory.
```
docker run --rm --user $(id -u):$(id -g) -v ${PWD}:$HOME/local openapitools/openapi-generator-cli generate -i $HOME/local/swagger_docs.yml -g bash -o $HOME/local/test 
```

4. create excel file and upload that on aifile.
5. write prepare.py script within /src directory somehow to fetch test files from proper address to proper directory.
6. run “make init” to fetch test files.
7. run “make dbud” to make the solution up and running.
6. check src/test directory it should includes at least client.sh for now. Add test_service_config_template.yml, test_service.py and requirements.txt file with proper content to this directory.
7. now you are able to to run tests with “make test” command.