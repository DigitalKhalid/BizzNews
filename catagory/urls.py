from django.urls import path
from . import views
from bizzsupport import error

urlpatterns = [
    path('panel/catagory/list', views.catagory_list, name='catagory_list'),
    path('panel/catagory/add', views.add_catagory, name='add_catagory'),
    path('panel/catagory/error', error, name='error'),
    path('panel/catagory/delete/<pk>', views.delete_catagory, name='delete_catagory'),
    path('panel/catagory/edit/<pk>', views.catagory_edit, name='catagory_edit')
]
