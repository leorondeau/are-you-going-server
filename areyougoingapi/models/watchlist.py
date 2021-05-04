from django.db import models
from django.db import User

class WatchList(models.Model):

    watcher = models.ForeignKey("Goer", on_delete=models.CASCADE)
    watched = models.ForeignKey("Goer", on_delete=models.CASCADE)
    watch = models.BooleanField(default=False, null=False)