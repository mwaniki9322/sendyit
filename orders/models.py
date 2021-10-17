from django.db import models
from authentication.models import User

# Create your models here.
class Orders(models.Model):

    owner=models.ForeignKey(to=User, on_delete=models.CASCADE)
    vehicle=models.CharField(max_length=255)
    description=models.TextField()
    pickup_location=models.CharField(max_length=255)
    destination=models.CharField(max_length=255)
    reciever_name=models.CharField(max_length=255)
    reciever_number=models.CharField(max_length=10)
    weight=models.CharField(max_length=255)
    date = models.DateField(null=False, blank=False)