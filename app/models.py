from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    mobile_number = models.CharField(
        _("Mobile Number"), max_length=14, unique=True)
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    date_of_birth = models.DateField(_("Date of Birth"), null=True)
    sex = models.BooleanField(_("Sex"), null=True)
    email = models.EmailField(_("Email"), max_length=254, unique=True)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
