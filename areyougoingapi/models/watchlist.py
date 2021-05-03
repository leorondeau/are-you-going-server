from django.db import models

class WatchList(models.Model):

    goer = models.ForeignKey("Goer", on_delete=models.CASCADE)
    watched_user = models.ForeignKey("Goer", on_delete=models.CASCADE)
    watch = models.BooleanField(default=False, null=False)