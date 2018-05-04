from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^homepage_1/', views.homepage_1, name="homepage_1"),
    url(r'^homepage_2/', views.homepage_2, name="homepage_2"),
]