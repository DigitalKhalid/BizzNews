from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('panel/', views.panel, name='panel'),
    path('login/', views.mylogin, name='mylogin'),
    path('panel/settings', views.site_settings, name='site_settings'),
    path('panel/settings/update/<username>', views.user_settings, name='user_settings'),
    path('contact/', views.contact, name='contact'),
]