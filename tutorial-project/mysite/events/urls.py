from django.urls import path
from . import views


urlpatterns = [
    path(r'esteban/$', views.index, name='index'),
    path('/$', views.individual_post, name='individual_post')
]