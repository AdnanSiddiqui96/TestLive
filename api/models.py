from django.db import models

# Create your models here.

    
class results(models.Model):

        name = models.CharField(max_length=255, default='')
        result = models.CharField(max_length=255, default='')

        def __str__(self):
            return self.name