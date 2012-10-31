from django.db import models



class Comments(models.Model):
    name = models.CharField(max_length=32)
    #email=models.CharField(max_length=64)
    subject = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    content = models.TextField()

    def __unicode__(self):
        return self.name

