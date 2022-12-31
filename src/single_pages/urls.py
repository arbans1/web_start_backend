from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.landing, name='landing'),
    path(route='about_me/', view=views.about_me, name='about_me'),
]
