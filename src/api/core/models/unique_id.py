from django.db import models
from django.utils.text import gettext_lazy as _
import time
import math
from .serialization_model import SerializationModel


# Create your models here.


class UniqueIDClass(models.Model, SerializationModel):
    id = models.CharField(
        _('id'),
        max_length=50,
        unique=True,
        primary_key=True,
        editable=False
    )

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.id = str(int(math.pow(10, 9) * time.time()))
        super(UniqueIDClass, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )
