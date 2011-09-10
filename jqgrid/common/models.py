from django.db import models

class Something(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=(('F', 'Female'), ('M', 'Male')))

    def __unicode__(self):
        return self.name
