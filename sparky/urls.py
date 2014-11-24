from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

handler404 = "sparky_landing.views.handler404"
handler500 = "sparky_landing.views.handler500"

urlpatterns = patterns('',
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    # Examples:
    url(r'^$', 'sparky_landing.views.index', name='home'),
    url(r'^save/', 'sparky_landing.views.save', name='save'), 
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
