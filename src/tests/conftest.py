import pytest



def pytest_addoption(parser):
    parser.addoption("--filepath", action="store", default='./config.yml', help="Path to config file for tests")
    # parser.addoption("--base-url", action="store", default='', help="ASSIGNMENT traefik url")    
    # parser.addoption("--sleep", action="store", default=0.5, help="Sleep time between each request. default: 0.5")


@pytest.fixture()
def filepath(request):
    return request.config.getoption("--filepath")

# @pytest.fixture()
# def base_url(request):
#     return request.config.getoption("--base-url")

# @pytest.fixture()
# def sleep(request):
#     return request.config.getoption("--sleep")
