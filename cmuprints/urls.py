from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cmuprints.views.home', name='home'),
    # url(r'^cmuprints/', include('cmuprints.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('index.urls')),
    url(r'^$', include('index.urls')),
    url(r'^about/',include('index.urls')),
    url(r'^printers/', include('index.urls'))
)
