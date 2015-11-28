from django.conf.urls import url

from django.conf.urls import include, url, patterns
from django.contrib import admin
from . import views


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^create_customer/$', views.create_customer, name='create_customer'),
    url(r'^show_customers/$', views.show_customers, name='show_customers'),
    url(r'^profile/(?P<customer_id>[0-9]+)/$', views.customer_profile, name='customer_profile'),
)

