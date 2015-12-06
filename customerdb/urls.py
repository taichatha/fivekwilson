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
    url(r'^(?P<customer_id>[0-9]+)/$', views.customer_profile, name='customer_profile'),
    url(r'^(?P<customer_id>[0-9]+)/add_car/$', views.add_car, name='add_car'),
    url(r'^(?P<customer_id>[0-9]+)/(?P<car_id>[0-9]+)/deletecar', views.delete_car, name="delete_car"),
    url(r'^(?P<customer_id>[0-9]+)/add_workorder', views.add_workorder, name="add_workorder"),
    url(r'^(?P<customer_id>[0-9]+)/(?P<appointment_id>[0-9]+)/deleteappt', views.delete_workorder, name="delete_workorder"),
)

