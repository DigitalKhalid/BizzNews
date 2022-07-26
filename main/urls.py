from django.urls import path
from . import views
from bizzsole.bizzfunc import error_front

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('panel/', views.panel, name='panel'),
    path('login/', views.mylogin, name='mylogin'),
    path('panel/settings', views.site_settings, name='site_settings'),
    path('panel/user/update/<username>', views.user_settings, name='user_settings'),
    path('panel/user/register', views.user_register, name='user_register'),
    path('contact/', views.contact, name='contact'),
    path('error/', error_front, name='error_front'),
]