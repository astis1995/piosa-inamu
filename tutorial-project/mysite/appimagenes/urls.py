from django.urls import path

from . import views
urlpatterns = [#path('a/', views.student_show, name = 'webpage_show'),
path('', views.webpage_show, name = 'webpage_show'),
]
