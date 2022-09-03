Forexampleapi

---
**Service Test**

In order to test files, use following format.

pytest -q file_name.py --filepath "config.yml"

use -s to show prints and -v to show more info


Example:

`pytest -q test_service.py --filepath "config.yml"`
`pytest -q test_service.py -s --filepath "config.yml"`
`pytest -q test_service.py -v --filepath "config.yml"`
`pytest -q test_service.py -s -v --filepath "config.yml"`

test_service tests a neural network model trained. you need to have train_catvnoncat.h5 and params.pkl file in /app_data/assingmentapi/data

test_overload tests service under high loads of request

test_ttutils_config_handler tests functionality of ttutils inorder to get parameters from environmet variables and config file
note: test_ttutils_config_handler does not need to pass config file as pytest argument
note: you may need to change headers in config.yaml to be authenticate by authacl
