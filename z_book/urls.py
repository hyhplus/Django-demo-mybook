from django.conf.urls import url
from z_book import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^index/$', views.index),

    url(r'pag(?P<pIndex>[0-9]*)/$', views.pagTest, name='pagTest'),

    url(r'^area/([0-9]+)/$', views.area, name='area'),

    url(r'^get1/$', views.getTest1),
    url(r'^get2/$', views.getTest2),
    url(r'^get3/$', views.getTest3),

    url(r'^post1/$', views.postTest1),
    url(r'^post2/$', views.postTest2),

    #url(r'^cookie/$', views.cookie),

    url(r'^polls1/$', views.indexhttp),

    url(r'^json/$', views.jsonIndex),

    url(r'^reverse/$', views.reverse1),
    url(r'^reverse/([0-9]+)/$', views.reverse2, name='reverse2')

]