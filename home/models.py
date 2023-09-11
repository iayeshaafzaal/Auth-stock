from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class UserData(AbstractUser):
    username = None
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    balance = models.CharField(max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class Stockdata(models.Model):
    ticker = models.CharField(max_length=20)
    open_price = models.IntegerField()
    close_price = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    volume = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)


class Transactiontable(models.Model):
    Type = (
        (0, "Buy"),
        (1, "sell")
    )
    transaction_id = models.CharField(max_length=10)
    user_id = models.CharField(max_length=10)
    ticker = models.CharField(max_length=20)
    transaction_type = models.IntegerField(choices=Type, default=0)
    transaction_volume = models.IntegerField()
    transaction_price = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
