from api.core import utils
import sys
import os
from ttutils.TTConfigHandler import confighandler
sys.path.insert(0, os.pardir)
# from data.config import current_dir as data_dir

IMAGE_MAX_WIDTH = confighandler.get_config('IMAGE_MAX_WIDTH', 800)
IMAGE_MIN_WIDTH = confighandler.get_config('IMAGE_MIN_WIDTH', 100)
IMAGE_MIN_HEIGHT = confighandler.get_config('IMAGE_MIN_HEIGHT', 100)
IMAGE_MAX_HEIGHT = confighandler.get_config('IMAGE_MAX_HEIGHT', 800)

