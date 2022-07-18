from django.urls import path
from . import views

urlpatterns = [
    path('contact/submit', views.contactform_submit, name='contactform_submit'),
    path('contact/list', views.contactform_list, name='contactform_list'),
    path('contact/status/<pk>', views.change_readstatus, name='change_readstatus'),
    path('contact/delete/<pk>', views.contactform_delete, name='contactform_delete'),
]