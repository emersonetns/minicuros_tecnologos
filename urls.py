from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'minicursos_tecnologos.views.home', name='home'),
    # url(r'^minicursos_tecnologos/', include('minicursos_tecnologos.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
