from django.db import models

# Create your models here.
class Tables(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    description = models.TextField('This is Empty TextField')

class Place(models.Model):
    name2 = models.CharField(max_length=250)
    image2 = models.ImageField(upload_to='img')
    description2 = models.TextField('Empty')



    def __str__(self):
        return self.name
    def __str__(self):
        return self.name2