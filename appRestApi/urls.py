from django.urls import re_path
from appRestApi import views 
 
urlpatterns = [ 
    re_path(r'^api/appRestApi$', views.appRestApi_list),
    re_path(r'^api/appRestApi/(?P<pk>[0-9]+)$', views.appRestApi_detail),
    re_path(r'^api/appRestApi/published$', views.appRestApi_list_published)
]