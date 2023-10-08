from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import AccountsManager


class UserAccounts(AbstractBaseUser):
    ##basic credentials
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    ##default fields
    is_verified = models.BooleanField(default=True )
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ##admin/superuser fields
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    ##creation options
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AccountsManager()   

    def __str__(self): 
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_staff

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser
