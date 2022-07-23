from django.urls import path
from . import views

urlpatterns = [
    path('panel/users/list', views.user_list, name='user_list'),
    path('panel/users/edit/<pk>', views.user_edit, name='user_edit'),
]
