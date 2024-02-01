from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("email is required")
        if not password:
            raise ValueError("password is required")

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        # extra_fields.pop('password')
        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email=email, password=password, **extra_fields)



# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError("email is required")
#         if not password:
#             raise ValueError("password is required")

#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.is_admin = False
#         user.is_staff = False

#         user.save()

#         return user

#     def create_superuser(self, email, password=None):
#         user = self.create_user(email=email, password=password)

#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True

#         user.save()

#         return user


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    is_creator = models.BooleanField(default=False)

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
