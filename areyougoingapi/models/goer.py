from django.db import models
from django.contrib.auth.models import User

class Goer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Goers')
    