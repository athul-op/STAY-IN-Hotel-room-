from django.db import models
from account.models import Account
# Create your models here.

class Room(models.Model):

    TYPES = (

        ('Single' , 'Single'),
        ( 'Double' , 'Double')
    )

    vendor_id      = models.ForeignKey(Account,on_delete=models.CASCADE)
    service        = models.CharField(max_length=100)
    price          = models.FloatField()
    image          = models.ImageField (upload_to="images")
    description    = models.TextField(max_length=1000)
    is_available   = models.BooleanField(default=True, verbose_name="available")
    is_verified    = models.BooleanField(default=False)
    has_ac         = models.BooleanField()
    type           = models.CharField(max_length=10, choices=TYPES)
    city           = models.CharField(max_length=100)
    district       = models.CharField(max_length=50,null=True)
    pin            = models.BigIntegerField()
    street         = models.CharField(max_length=50,null=True)
