from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.base),
    path('<int:id>/add', views.add),
    path('<int:id>/delete', views.delete),
]
