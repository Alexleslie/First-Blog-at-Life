from django.conf.urls import url,include
from . import views
from django.conf.urls import handler404, handler500
app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^post/(?P<pk>[0-9]+)/', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
    url(r'^outside/$', views.outside, name='outside'),
    url(r'^message/$', views.message, name='message'),
    url(r'^register/$', views.register, name='register'),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^edit_post/(?P<pk>[0-9]+)/$', views.edit, name='edit'),
    url(r'^create/', views.create, name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/', views.delete, name='delete'),
    url(r'news/', views.NewsView.as_view(), name='news'),
]
