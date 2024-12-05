from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Book(models.Model):
    name = models.CharField(_("book"), max_length=50)
    description = models.TextField(_("description"),max_length=100)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("")

    def __str__(self):
        return self.name

