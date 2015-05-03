"""This module contains url configuration.

Include your API resources and views into urlpatterns
"""
from django.conf.urls import patterns, include, url
from disqus_be.core_app.api import CommentResource
from django.contrib import admin

comment_resource = CommentResource()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/v1/', include(comment_resource.urls)),
)
