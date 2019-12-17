from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.base),
    re_path('', views.nnsss),
    re_path('', views.n_s_n),
    re_path('', views.phone),
]
