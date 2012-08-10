from django.db import models

# Create your models here.
class Sorteo(models.Model):
    name = models.CharField(max_length=200)
    digits = models.CharField(max_length=3)

    def __unicode__(self):
        return self.name + " " + self.digits
