from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


import sys, os
# Create your models here.

def getTemplates():
    templates = []
    templateLocation = os.path.dirname(os.path.normpath(__file__)) + '/templates/'
    for root, dirs, files in os.walk(templateLocation):
        for file in files:
            if file.endswith('.html') :
                templates.append((file,file))
    return templates

class Page(models.Model):
    title    = models.CharField(max_length=120, null=True)
    url      = models.CharField(max_length=120, null=True)
    template = models.CharField(max_length=120, null=True, choices=getTemplates())
    content = RichTextField(config_name='awesome_ckeditor')
    published  = models.BooleanField(default=False)
    access   = models.CharField(max_length=120, null=True, default='public', choices=[('public','public'),('authenticated','authenticated')])
    author   = models.ForeignKey(User,null=True)
    createdate  = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated     = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return "/page/admin"
