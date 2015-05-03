"""This module contains DB models"""
from django.db import models
from django.utils import timezone
# from core_app import utils
# from hashlib import md5

# Here we create Model
# 5 primary fields, url for storing URL of tab, text for storing written comment
# email for storing email of author, author for storing name of author of comment
# and pub_date for storing publishing date


class Comment(models.Model):

    url = models.CharField(max_length=1000)
    text = models.TextField()
    email = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=timezone.now)
