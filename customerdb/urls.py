from django.conf.urls import url

from django.conf.urls import include, url, patterns
from django.contrib import admin
from . import views


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^create_customer/$', views.create_customer, name='create_customer'),
)

