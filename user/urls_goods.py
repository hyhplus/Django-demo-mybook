from django.conf.urls import url
from user import views_goods, viewsUtil

urlpatterns = [
    url(r'^$', views_goods.index),
    url(r'^list/$', views_goods.goods_list),
    url(r'^pwd/$',views_goods.user_pwd),

    url(r'^v/$', viewsUtil.verifycode),
    url(r'^vhandle/$', viewsUtil.verifycodeVaild),
    url(r'^getcode/$', viewsUtil.getcode),
]