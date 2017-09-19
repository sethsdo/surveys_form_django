from django.conf.urls import url
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),     
    url(r'^process/$', views.about),
    url(r'^result/$', views.result),
    url(r'^back/$', views.back)
]
