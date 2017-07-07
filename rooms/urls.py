from django.conf.urls import url

from . import views

app_name = 'rooms'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^show/(?P<room_id>[0-9]+)/$', views.show, name='show'),
    url(r'^new/$', views.new, name = 'new'),

]
