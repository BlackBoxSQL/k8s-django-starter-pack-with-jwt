from django.contrib.auth.models import AbstractUser
from django.db import models
from ..managers import UserManager, UserSoftManager
from core.models import UniqueIDClass, AuditableClass


class User(AbstractUser, UniqueIDClass, AuditableClass):
    full_name = models.CharField(max_length=200, null=True, blank=True)

    REQUIRED_FIELDS = []

    objects = UserManager()
    soft_manager = UserSoftManager()

    def save(self, *args, **kwargs):
        self._generate_full_name()
        super(User, self).save(*args, **kwargs)

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return ''

    def _generate_full_name(self):
        t = []
        if self.first_name:
            t.append(self.first_name)
        if self.last_name:
            t.append(self.last_name)
        if t:
            self.full_name = ' '.join(t)
        else:
            self.full_name = None

    class Meta:
        db_table = 'users'

