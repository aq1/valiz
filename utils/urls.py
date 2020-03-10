from django.conf.urls import url

from .views import log


urlpatterns = [
    url(r'^log/$', log, name='log'),
]
