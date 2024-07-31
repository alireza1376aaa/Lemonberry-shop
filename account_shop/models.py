from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import base_user
from django.utils.translation import gettext_lazy as _


# Create your models here.


class CustomUserManager(base_user.BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class autentication(AbstractUser):
    username = None
    image_pro = models.ImageField(upload_to='upload/upload/%Y/%m/%d', null=True, blank=True,
                                  default='upload/profile/defult_pro.png')
    addres = models.CharField(max_length=100, null=True, blank=True)
    phone = PhoneNumberField(unique=True)
    verify_code = models.CharField(max_length=100,unique=True)
    is_verify = models.BooleanField(default=False)
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']
    objects = CustomUserManager()
    def __str__(self):
        return self.email
    class Meta:
        verbose_name = 'اهراز هویت '
        verbose_name_plural = 'اهراز هویت ها'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolut_url(self):
        return reverse('details_user_p', kwargs={'pk': self.id})
