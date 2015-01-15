from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=5)
    count = models.IntegerField()

#    def __unicode__(self):
#        return self.title
