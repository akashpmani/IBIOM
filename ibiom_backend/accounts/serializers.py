from rest_framework import serializers
from accounts.models import UserAccounts
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class UserRegistrationSerializer(serializers.ModelSerializer):
    # We are writing this becoz we need confirm password field in our Registratin Request
    class Meta:
        model = UserAccounts
        fields=['email', 'username', 'password', 'phone']
        extra_kwargs={
        'password':{'write_only':True}
        }

    # Validating Password and Confirm Password while Registration
    def create(self, validate_data):
        return UserAccounts.objects.create_user(**validate_data)

    
# class UserLoginSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(max_length=255)
#     class Meta:
#         model = User
#         fields = ['email', 'password']