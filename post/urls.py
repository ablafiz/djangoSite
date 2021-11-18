from django.urls import path
from post import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]