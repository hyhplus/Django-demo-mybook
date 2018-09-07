from user import views
from django.conf.urls import url

urlpatterns = [
    url('^test/$', views.test),

    url(r'^index/$', views.index),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_handle/$', views.login_handle),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^$', views.ajaxIndex),
    url(r'^area/$', views.getArea1),
    url(r'^([0-9]+)/$', views.getArea2),

    url(r'^cache/$', views.cacheIndex),
]