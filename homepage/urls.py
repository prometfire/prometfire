from django.conf.urls import patterns, include, url

# from .views import homepage_view

urlpatterns = patterns('homepage.views',
    # Examples:
    url(r'^$', 'homepage_view'),
    # url(r'^prometfire/', include('prometfire.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
