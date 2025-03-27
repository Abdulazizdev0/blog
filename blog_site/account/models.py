from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password,check_password

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError(_("The email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        print(user.password)
        user.is_staff = True
        user.is_active = True
        user.save()
        return user

    def create_superuser(self,email,password, **extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Super user must have is_staff = True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser = True"))
        print('SUPERUSER')
        return self.create_user(email,password, **extra_fields)



class CustomUser(AbstractUser):
    email = models.CharField(max_length=100,unique=True)
    username = None
    first_name = models.CharField(max_length=222,null=True,blank=True)
    last_name = models.CharField(max_length=222,null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)
    #     self._password = raw_password

    def __str__(self):
        return self.email