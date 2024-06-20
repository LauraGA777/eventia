from django.db import models

# Create your models here.

class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
