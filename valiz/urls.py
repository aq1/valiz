from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


from main.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^schedule/$', schedule, name='schedule'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^photo/$', photo, name='photo'),
    url(r'^price/$', price, name='price'),
    url(r'^doctors/$', doctors, name='doctors'),
    url(r'^documents/$', documents, name='documents'),
    url(r'^documents/(?P<pk>\d+)$', document, name='document'),
    url(r'^announcements/$', announcements, name='announcements'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
