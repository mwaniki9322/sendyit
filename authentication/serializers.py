from django.db.models.base import Model
from rest_framework import serializers
from rest_framework.utils import field_mapping
from . models import User, UserManager
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)


    class Meta:
        model=User
        fields=['email','username','password']
    
    def validate(self, attrs):
        email = attrs.get('email','')
        username=attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token=serializers.CharField(max_length=555)

    class Meta:
        model=User
        fields=['token']

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255,min_length=3)
    password = serializers.CharField(max_length=68,min_length=6,write_only = True)
    username = serializers.CharField(max_length=68,min_length=3,read_only=True)
    tokens = serializers.CharField(max_length=68,min_length=6,read_only=True)
    class Meta:
        model = User
        fields = ['email','password','username','tokens']
    def validate(self,attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')
        
        user = auth.authenticate(email = email,password=password)
        if not user:
                raise AuthenticationFailed('Invalid credentials,try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled,contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
        return{
            'email':user.email,
            'username':user.username,
            'tokens':user.tokens
        }
        return super().validate(attrs)