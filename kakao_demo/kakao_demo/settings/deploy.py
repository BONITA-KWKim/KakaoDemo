from ..conf.util import get_server_info_value
from .base import *

SETTING_PRD_DIC = get_server_info_value("deployment")
SECRET_KEY = SETTING_PRD_DIC["SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'kakao_demo.wsgi.deploy.application'

