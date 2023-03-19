from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctors')
    qualification = models.CharField(max_length=100)
    details = models.TextField()
    tags = models.CharField(max_length=100)
    rating = models.IntegerField()
    price_range = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.name
