from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from mainapp.models import NULLABLE


class CustomUser(AbstractUser):
    username_validator = ASCIIUsernameValidator()

    email = models.EmailField(
        _('Email'),
        max_length=256,
        blank=True,
        # unique=True,
        # error_messages={
        #     "unique": _("A user with that email address already exists"),
        # }
    )
    age = models.PositiveSmallIntegerField(**NULLABLE)
    avatar = models.ImageField(
        upload_to='users',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'




