from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Хешируем пароль
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('Role', 'admin')
        return self.create_user(username, password, **extra_fields)

class Users(AbstractBaseUser):
    UserID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Pytronumic = models.CharField(max_length=255)
    Username = models.CharField(max_length=255, unique=True)
    Role = models.CharField(max_length=50)
    Email = models.EmailField(max_length=255, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'Username'
    REQUIRED_FIELDS = ['Email', 'Role']

    def __str__(self):
        return self.Username

    class Meta:
        db_table = 'Users'  # Указываем имя таблицы