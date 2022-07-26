from django.urls import path
from . import views

urlpatterns = [
    path('panel/users/list', views.user_list, name='user_list'),
    path('panel/users/edit/<pk>', views.user_edit, name='user_edit'),
    path('panel/users/delete/<pk>', views.user_delete, name='user_delete'),
    path('panel/users/groups', views.user_group, name='user_group'),
    path('panel/users/groups/add', views.user_group_add, name='user_group_add'),
    path('panel/users/groups/delete/<pk>', views.user_group_delete, name='user_group_delete'),
    path('panel/users/groups/assign/<pk>', views.user_addgroup, name='user_addgroup'),
    path('panel/users/groups/delete/<pk>/<groupname>', views.user_deletegroup, name='user_deletegroup'),
    path('panel/users/groups/edit/<pk>', views.user_group_edit, name='user_group_edit'),
    path('panel/users/permissions', views.permissions_list, name='permissions_list'),
    path('panel/users/permissions/add', views.permissions_add, name='permissions_add'),
    path('panel/users/permissions/delete/<pk>', views.permissions_delete, name='permissions_delete'),
    path('panel/users/permissions/edit/<pk>', views.permissions_edit, name='permissions_edit'),
    path('panel/users/permissions/assign/<pk>', views.user_addpermission, name='user_addpermission'),
    path('panel/users/permissions/delete/<pk>/<permissionname>', views.user_deletepermission, name='user_deletepermission'),
]
