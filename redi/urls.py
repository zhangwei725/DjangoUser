from django.conf.urls import url, include
from django.contrib import admin

from redi import views

urlpatterns = [
    url('1/', views.redi1),
    url('2/', views.redi2),
    url('3/', views.redi3),

]
