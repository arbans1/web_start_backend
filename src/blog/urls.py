from django.urls import path
from . import views

urlpatterns = [
    # index 페이지 추가
    path(route='', view=views.index),

    # single_post 페이지 추가
    path(route='<int:pk>/', view=views.single_post_page, name='single_post_page'),

]
