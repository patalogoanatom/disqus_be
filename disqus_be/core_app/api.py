"""This module contains API resource classes"""
from tastypie.resources import ModelResource
from core_app.models import Comment
from tastypie.authorization import Authorization
from tastypie import fields
# from core_app import utils


class CommentResource(ModelResource):
    url = fields.CharField(attribute="url")
    text = fields.CharField(attribute="text")
    email = fields.CharField(attribute="email")
    author = fields.CharField(attribute="author")

    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        authorization = Authorization()
        always_return_data = True
