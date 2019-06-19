from django.conf.urls import url
from . import views

app_name = 'recipie_app'

urlpatterns = [
    url(r'^$', views.recipie_list, name='home'),
    url(r'^create', views.create_recipie, name='create'),
    # url(r'^(?P<recipie_id>[0-9]+)/detail/$', views.detail, name='detail'),
]