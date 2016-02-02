from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /operators/
    url(r'^$', views.index, name='index'),
    # ex: /operators/5/
    url(r'^(?P<name_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /operators/5/results/
    url(r'^(?P<name_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /operators/5/change_destination/
    url(r'^(?P<name_id>[0-9]+)/change_destination/$', views.change_destination, name='change_destination'),
]