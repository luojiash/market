from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'market_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('Login.urls')),
    url(r'^accounts/', include('Buyer.urls')),
	url(r'^accounts/', include('Saleman.urls')),
    url(r'^accounts/', include('Manager.urls')),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.STATICFILES_DIRS}), 
)
