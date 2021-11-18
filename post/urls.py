from django.urls import path
from post import views

urlpatterns = [
    path('index', views.post_list, name='post_list'),
    path('index1', views.myname, name='myname'),
]