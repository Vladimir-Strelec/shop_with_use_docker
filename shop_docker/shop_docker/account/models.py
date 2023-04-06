from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _

from account.custom_validators import check_only_characters_in_name


class UserShop(models.Model):
    name = models.CharField('Name', max_length=150, validators=(MinLengthValidator(3), check_only_characters_in_name),)
    password = models.CharField('Password', max_length=50,)
    email = models.EmailField('Email', unique=True, error_messages={
        'unique': "A Email with that Emails already exists."},)

    data_joined = models.DateTimeField('Data joined', default=timezone.now,)
    data_change_info = models.DateTimeField('Data change info', auto_now=True,)
    is_active = models.BooleanField(default=False,)
    auth_user = models.BooleanField(default=False,)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return f"{self.name} - {self.email}"