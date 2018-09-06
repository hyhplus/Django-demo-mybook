from user import views
from django.conf.urls import url

urlpatterns = [
    url('^test/$', views.test),

    url(r'^index/$', views.index),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_handle/$', views.login_handle),
    url(r'^logout/$', views.logout, name='logout'),


]