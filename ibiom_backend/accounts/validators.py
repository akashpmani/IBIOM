from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework import status
UserModel = get_user_model()
from rest_framework import serializers


def custom_validation(data):
    try:
        email = data['email'].strip()
        username = data['username'].strip()
        password = data['password'].strip()
    except:
        raise serializers.ValidationError({'Invalid credentials': 'Please  Give Proper Credentials'})
    
    if not email or UserModel.objects.filter(email=email).exists():
        raise serializers.ValidationError({'email': 'Choose another email'})
    
    if not password or len(password) < 8:
        raise serializers.ValidationError({'password': 'Choose another password, minimum 8 characters'})
    
    if not username or UserModel.objects.filter(username=username).exists():
        raise serializers.ValidationError({'username': 'Choose another username'})
    
    return data
    
def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError('an email is needed')
    return True

def validate_logincred(data):
    if data:
        if '@' in data and '.' in data:
            return data
        if data.isalnum():
            return data
    raise ValidationError('Invalid email/username format')

def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('choose another username')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('a password is needed')
    return True