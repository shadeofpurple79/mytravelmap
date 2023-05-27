from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Destination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    month_year_visited = models.DateField(null=True, blank=True)
    month_year_to_visit = models.DataField(null=True, blank=True)

    EXPERIENCE_OPTIONS = (
        ('visited', 'I have visited'),
        ('want_to_visit', 'I want to visit'),
    )
    experience_option = models.CharField(
        max_length=50, choices=EXPERIENCE_OPTIONS, default='visited'
    )

class Food(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')

    def_str_(self):
        return self.name