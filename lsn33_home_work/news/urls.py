from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='news_base'),
    path('new/', views.new, name='news_new'),
    path('edit/', views.edit, name='news_edit'),
    path('lock/', views.lock, name='news_lock'),
]
