from django.conf.urls.defaults import patterns, include, url
from mysite.books import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^grappelli/',include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/$',views.main_form),
    url(r'^search-form/$',views.search_form),
    url(r'^search/$',views.search_book),

    url(r'^search_author-form/$',views.search_author_form),
    url(r'^search_author/$',views.search_author),
    
)
