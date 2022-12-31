from django.urls import path
from . import views

urlpatterns = [
    # index 페이지 추가
    # path(route='', view=views.index),
    path(route='', view=views.PostList.as_view(), name='index'),

    # single_post 페이지 추가
    # path(route='<int:pk>/', view=views.single_post_page, name='single_post_page'),
    path(route='<int:pk>/', view=views.PostDetail.as_view(), name='single_post_page'),

]
