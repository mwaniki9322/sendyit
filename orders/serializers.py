from django.db.models import fields
from rest_framework import serializers 
from .models import Orders



class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model=Orders
        fields=['owner_id','id','date','vehicle','description','pickup_location','destination','reciever_name','reciever_number','weight']
