from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.base),
    re_path(r'^(?P<page>\d{2}[A-z]{3})/$', views.any_right),
    re_path(r'^(?P<page>\d-[A-z]-\d)/$', views.any_right),
    re_path(r'^(?P<page>(050|066|095|099|039|067|068|096|097|098|063|093|091|092|094)-\d{3}(-\d\d){2})/$',
            views.any_right),
]
