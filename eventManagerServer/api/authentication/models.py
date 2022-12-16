from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class Role(models.Model):
    role = models.CharField(unique=True, max_length=50, null=False)


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email not provided")
        if not password:
            raise ValueError("password not provided")

        user = self.model(
            email=self.normalize_email(email),
                   ** extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', Role.objects.get(id = 4))
        user = self._create_user(email, password, **extra_fields)
        user.first_name = first_name
        user.last_name = last_name
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, models.Model):
    email = models.EmailField(unique=True, max_length=254)
    first_name = models.CharField(max_length=240, null=True)
    last_name = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=240, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    objects = UserManager()
