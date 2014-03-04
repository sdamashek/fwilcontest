from django.conf.urls import patterns, url, include
from rest_framework import routers

from usermanagement import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'customers', views.CustomerViewSet)


urlpatterns = patterns('',
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^api/', include(router.urls)),
                       url(r'^$', views.index, name='index'),
                       url(r'^manage/$', views.manage, name='manage'),
                       url(r'^manage/user/new/$', views.add_user),
                       url(r'^manage/user/edit/(?P<id>\d+)/$', views.add_user),
                       url(r'^manage/user/$', views.view_user),
                       url(r'^manage/item/new/$', views.add_edit_item),
                       url(r'^manage/item/edit/(?P<id>\d+)/$', views.add_edit_item),
                       url(r'^manage/item/$', views.view_item),
                       url(r'^manage/item/delete/$', views.delete_item),
                       url(r'^manage/category/new/$', views.add_edit_category),
                       url(r'^manage/category/edit/(?P<id>\d+)/$', views.add_edit_category),
                       url(r'^manage/category/$', views.view_category),
                       url(r'^manage/category/delete/$', views.delete_category),
                       url(r'^manage/customer/new/$', views.add_edit_customer),
                       url(r'^manage/customer/edit/(?P<id>\d+)/$', views.add_edit_customer),
                       url(r'^manage/customer/$', views.view_customer),
                       url(r'^manage/customer/delete/$', views.delete_customer),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^logout/$', views.logout_view),
                       )
