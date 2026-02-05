from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'email est obligatoire")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superuser doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Le superuser doit avoir is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    NIVEAU_STUDENT = [
        ('2ndeA', '2ndeA'),
        ('2ndeC', '2ndeC'),
        ('1éreA', '1éreA'),
        ('1éreC', '1éreC'),
        ('1éreD', '1éreD'),
        ('TleA', 'TleA'),
        ('TleC', 'TleC'),
        ('TleD', 'TleD'),
        ('L1_INFO', 'L1 INFO'),
        ('L2_INFO', 'L2 INFO'),
        ('L3_INFO', 'L3 INFO'),

    ]

    classe = models.CharField(max_length=20, choices=NIVEAU_STUDENT, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.email}, {self.classe}, {self.last_name}, {self.first_name}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="profile_images", default='image.png', blank=True, null=True)
    ecole = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.user.first_name},  {self.user.last_name}"
