from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('<int:id>/', views.id_base),
    path('<int:id>/add', views.id_add),
    path('<int:id>/delete', views.id_delete),
]
