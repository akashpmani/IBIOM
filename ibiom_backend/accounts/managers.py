
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

# create custom manager


class AccountsManager(BaseUserManager):
    """
      Creates and saves a User with the given email, name, and password.

    """

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The username field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        user = self.create_user(email=email,
                                username=username , password=password)
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    def create_staff(self, email, username, password=None, **extra_fields):
        user = self.create_user(email=email,
                                username=username, password=password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def authenticate(self, request, login_cred=None, password=None ):
        print("authernticate")
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(email=login_cred) | Q(username=login_cred))
        except UserModel.DoesNotExist:
            print('no user')
            return None
        else:
            if user and check_password(password, user.password):
                return user
        return None

    def getuser(self, request, email=None, password=None, username=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(email=email) | Q(username=username))
        except UserModel.DoesNotExist:
            return None
        return user
