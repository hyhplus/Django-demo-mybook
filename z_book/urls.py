from django.conf.urls import url
from z_book import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^index/$', views.index),

]