from django.conf.urls import url
from z_book import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^index/$', views.index),

    url(r'^area/([0-9]+)/$', views.area, name='area'),

    url(r'^get1/$', views.getTest1),
    url(r'^get2/$', views.getTest2),
    url(r'^get3/$', views.getTest3),

    url(r'^post1/$', views.postTest1),
    url(r'^post2/$', views.postTest2),

    url(r'^cookie/$', views.cookie),

]