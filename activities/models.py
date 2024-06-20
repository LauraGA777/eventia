from django.db import models

# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    participant = models.ForeignKey('participants.Participant', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

