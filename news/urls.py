from django.urls import path
from . import views
from bizzsupport import error

urlpatterns = [
    path('news/<pk>', views.news_detail, name='news_detail'),
    path('panel/news/list', views.news_list, name='news_list'),
    path('panel/news/add', views.add_news, name='add_news'),
    path('panel/news/error', error, name='error'),
    path('panel/news/delete/<pk>', views.delete_news, name='delete_news'),
    path('panel/news/edit/<pk>', views.edit_news, name='edit_news')
]
