from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name


