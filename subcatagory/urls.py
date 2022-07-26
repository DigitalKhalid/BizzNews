from django.urls import path
from . import views
from bizzsole.bizzfunc import error

urlpatterns = [
    path('panel/subcatagory/list', views.subcatagory_list, name='subcatagory_list'),
    path('panel/subcatagory/add', views.add_subcatagory, name='add_subcatagory'),
    path('panel/subcatagory/error', error, name='error'),
    path('panel/subcatagory/delete/<pk>', views.delete_subcatagory, name='delete_subcatagory'),
    path('panel/subcatagory/edit/<pk>', views.subcatagory_edit, name='subcatagory_edit')
]