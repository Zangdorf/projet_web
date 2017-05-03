from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible #Necesario usando python3 ??
from django.core.validators import MinValueValidator


class Member(models.Model):
    name = models.CharField(
        max_length=40,
        help_text = "Name, Prenom, Nombre"
        )
    last_name = models.CharField(
        max_length=40,
        help_text = "Family name, Nom, Apellidos"
        )
    email = models.EmailField(
        max_length = 100,
        unique = True,
        help_text = "Enter email like exemple@domain.com"
        )
    active_member = models.BooleanField(
        default=False,
        help_text = "Do you want to become an active member? :)"
        )

    def get_name(self):
        return self.name

    def get_last_name(self):
        return self.last_name

    def get_mail(self):
        return self.email

    def get_actif_member(self):
        return active_member

    def __str__(self):
        return "%s %s %s" % (self.name, self.last_name, self.email)
