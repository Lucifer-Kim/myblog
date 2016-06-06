from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^about$', views.about, name='about'),
    url(r'^$', views.post_list, name='post_list'),
]
