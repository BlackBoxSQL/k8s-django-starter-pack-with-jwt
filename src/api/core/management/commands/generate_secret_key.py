from django.core.management.base import BaseCommand, CommandError
from typing import Any
import string
import random


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        list_of_characters = string.ascii_letters+string.digits+string.punctuation
        s = ''.join([random.choice(list_of_characters) for i in range(0, 50)])
        print(s)
