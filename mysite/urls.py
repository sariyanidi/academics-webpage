from django.conf.urls import patterns, include, url
from blog.views import PublicationsView, ProjectsView, ProjectView, ResourcesView, \
                       CodeSnippetsView, ArticleView, ArticlesView, IndexView, AboutView

from django.conf import settings

from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'personal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', IndexView.as_view(),name='index'),
    url(r'^index.*$', IndexView.as_view(),name='index'),
    url(r'^about/', AboutView.as_view(),name='about'),
    url(r'^project/((?P<slug>[-\w]+))/(?P<id>\d+)/$', ProjectView.as_view(),name='project'),
    url(r'^projects/$', ProjectsView.as_view(),name='projects'),
    url(r'^article/(?P<id>\d+)/$', ArticleView.as_view(),name='article'),
    url(r'^article/(?P<slug>[-\w]+)/(?P<id>\d+)/$', ArticleView.as_view(),name='article'),
    url(r'^articles/$', ArticlesView.as_view(),name='articles'),
    url(r'^articles/(?P<slug>[-\w]+)/(?P<id>\d+)/$', ArticlesView.as_view(),name='articles'),
    url(r'^resources/$', ResourcesView.as_view(),name='resources'),
    url(r'^code_snippets/$', CodeSnippetsView.as_view(),name='code_snippets'),
    url(r'^publications/$', PublicationsView.as_view(),name='publications'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include("grappelli.urls")), # grappelli URLS
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
   # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
