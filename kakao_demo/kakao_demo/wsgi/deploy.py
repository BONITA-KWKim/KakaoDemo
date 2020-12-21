import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kakao_demo.settings.deploy')

application = get_wsgi_application()

