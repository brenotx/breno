from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', RedirectView.as_view(pattern_name='blog:post-list'), name='go-to-blog'),

    url(r'^blog/', include('blog.urls', namespace="blog")),

    url(r'^admin/', include(admin.site.urls)),
)
