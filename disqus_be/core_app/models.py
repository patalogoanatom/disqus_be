"""This module contains DB models"""
from django.db import models
from django.utils import timezone
# from core_app import utils
from hashlib import md5


class Comment(models.Model):

    url = models.CharField(max_length=1000)
    text = models.TextField()
    email = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=timezone.now)
