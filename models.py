from django.db import models
from django.contrib.auth.models import User


class houses(models.Model):

    title = models.CharField('Title', max_length=50)
    state = models.CharField('State', null=True , max_length=50)
    location = models.CharField('Location', max_length=300)
    area = models.BigIntegerField('Area',)
    rooms = models.IntegerField(verbose_name="Rooms", null= True)
    bathrooms = models.IntegerField(verbose_name="Bathrooms", null= True )
    pic = models.ImageField(upload_to= 'pictures/')
    price = models.CharField('Price', max_length=50 )
    clas = models.ForeignKey(User, on_delete=models.CASCADE, null= True)

    objects = models.Manager()

    def __str__(self):
        return self.title

