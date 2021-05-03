from django.db import models

class Event(models.Model):

    goer = models.ForeignKey("Goer", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    startDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    details = models.CharField(max_length=150)
