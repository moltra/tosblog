from django.conf.urls import patterns, include, url
from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,}

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('zinnia.urls', namespace='zinnia')),
    # url(r'^blog/', include('blog.urls')),
	url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
	url(r'^comments/', include('django_comments.urls')),
	url(r'^tinymce/', include('tinymce.urls')), 
    url(r'^tinymce/zinnia/', include('zinnia_tinymce.urls')),
	url(r'^contact/', include('envelope.urls')),
    url(r'^admin/', include(admin.site.urls)),
)





urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
        {'sitemaps': sitemaps}),)