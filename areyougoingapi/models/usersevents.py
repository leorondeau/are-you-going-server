from django.db import models

class UsersEvents(models.Model):

    goer = models.ForeignKey("Goer", on_delete=models.CASCADE)
    event = models.ForeignKey("Goer", on_delete=models.CASCADE)
    