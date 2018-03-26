from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


from main.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^schedule/$', schedule),
    url(r'^contacts/$', contacts),
    url(r'^photo/$', photo),
    url(r'^price/$', price),
    url(r'^doctors/$', doctors),
    url(r'^documents/$', documents),
    url(r'^documents/(?P<pk>\d+)$', document),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
