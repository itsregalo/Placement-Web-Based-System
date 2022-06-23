from enum import unique
from django.db import models
# from django.db import models

# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import  BaseUserManager

# class MyAccountManager(BaseUserManager):
#     def create_user(self, username, phone, password=None):
#         if not username:
#             raise ValueError('Users must have a username')

#         user = self.model(
#             phone=phone,
#             username=username,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,  username, phone, password):
#         user = self.create_user(
#             password=password,
#             phone=phone,
#             username=username,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)


# class Account(AbstractUser):
#     phone = models.CharField(max_length=255,blank=True,null=True,unique=True)
#     username = models.CharField(max_length=6,blank=True,null=True)
#     country = models.CharField(max_length=6,blank=True,null=True)
#     otp = models.ForeignKey("otp.Otps", blank=True,
#                             null=True, on_delete=models.CASCADE)

#     is_parent = models.BooleanField(default=False)
#     is_parent = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     is_super_admin = models.BooleanField(default=False)

#     USERNAME_FIELD = 'phone'
#     REQUIRED_FIELDS = ['username']

#     objects = MyAccountManager()

#     def __str__(self):
#         return f'{self.username} - {self.phone}'
    
#     class Meta:
#         pass
    

from email.policy import default
import uuid
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

class MyAccountManager(BaseUserManager):
    @property
    def is_anonymous(self):
        return False
    def create_user(self, email, user_name, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not user_name:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            user_name=user_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, phone_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            phone_number=phone_number,
            user_name=user_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

USER_TYPE_CHOICES = (
      (1, 'Parent'),
      (2, 'Child'),
     )

wants = (
    ('1', 'Male'),
    ('2', 'Female'),
    ('2', 'Bi-Sex')
)

gender = (
    ('1', 'Male'),
    ('2', 'Female'),
)

STATUS = (("Organization", "Organization"), ("Student", "Student"))

class Account(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    password = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True,unique=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=255,null=True,blank=True)
    wants = models.CharField(max_length=255,null=True,blank=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    role =  models.CharField(choices=STATUS,default="Student",max_length=25)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.role == "Organization":
            self.is_organization == True
        
        if self.role == "Student":
            self.is_student == True

        super(Account, self).save(*args, **kwargs)

    # is_anonymous = False
    # is_authenticated = True

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','phone_number']

    objects = MyAccountManager()

    class Meta:
        db_table = "tbl_accounts"
