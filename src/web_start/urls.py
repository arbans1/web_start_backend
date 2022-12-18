"""Web_Start URL 구성

`urlpatterns '목록은 URL을 뷰로 라우팅합니다.자세한 내용은 다음을 참조하십시오.
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
예 :
기능보기
    1. 가져 오기 추가 : my_app 가져 오기 뷰에서
    2. urlpatterns에 URL을 추가하십시오 : Path ( '', views.home, name = 'home')
수업 기반 견해
    1. 가져 오기 추가 : Other_App.Views home에서 가져 오기
    2. urlpatterns에 URL을 추가하십시오 : Path ( '', home.as_view (), name = 'home')
다른 urlconf를 포함합니다
    1. 포함 () 함수 가져 오기 : django.urls import 포함, 경로
    2. urlpatterns에 URL 추가 : Path ( 'blog/', 포함 ( 'blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(route='admin/', view=admin.site.urls),

    # 사용자 설정
    path(route='blog/', view=include('blog.urls'), name='blog'),
]
