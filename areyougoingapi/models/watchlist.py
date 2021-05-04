from django.db import models
from .goer import Goer


class WatchList(models.Model):
    
    goer = models.ForeignKey(Goer, related_name='goer', on_delete=models.CASCADE)
    watched_user = models.ForeignKey(Goer, related_name='watched_user', on_delete=models.CASCADE)
    watch = models.BooleanField(default=False, null=False)

