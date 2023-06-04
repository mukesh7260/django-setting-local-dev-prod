from django.db import models

# Create your models here.

class Mouse(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    date = models.DateTimeField() 

    def __str__(self): 
        return self.name 
