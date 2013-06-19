from django.conf.urls import patterns, include, url

urlpatterns = patterns('homepage.views',
    url(r'^$', 'homepage_view'),
    url(r'^welcome/', 'welcome_view'),
    url(r'^form/', 'form_view'),
    url(r'^form_handler/', 'form_handler'),
)