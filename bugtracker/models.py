# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(default=False)
    user = models.ForeignKey(User,)

    def __unicode__(self):
        return self.title
