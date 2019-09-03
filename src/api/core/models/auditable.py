from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel, SoftDeletableManager
from .serialization_model import SerializationModel


class AuditableClass(SoftDeletableModel, TimeStampedModel, SerializationModel):
    objects = models.Manager()
    soft_manager = SoftDeletableManager()

    class Meta:
        abstract = True
