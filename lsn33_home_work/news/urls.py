from django.urls import path, re_path
from . import views

urlpatterns = [
    # level 01
    path('', views.base),
    path('new/', views.new),
    path('edit/', views.edit),
    path('lock/', views.lock),

    # level 02
    path('<int:id>/', views.id_base),
    path('<int:id>/add', views.id_add),
    path('<int:id>/delete', views.id_delete),

    # level 03
    re_path(r'^(?P<page>\d{2}[A-z]{3})/$', views.any_right),
    re_path(r'^(?P<page>\d-[A-z]-\d)/$', views.any_right),
    re_path(r'^(?P<page>(050|066|095|099|039|067|068|096|097|098|063|093|091|092|094)-\d{3}(-\d\d){2})/$',
            views.any_right),
]
