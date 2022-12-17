"""
Web_Start 프로젝트에 대한 ASGI 구성.

``Application``이라는 이름의 모듈 레벨 변수로 ASGI 호출을 노출시킵니다.

이 파일에 대한 자세한 내용은 참조하십시오
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_start.settings')

application = get_asgi_application()
