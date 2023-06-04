from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField

class Destination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    country_name = CountryField(blank_label='Country', null=False, blank=False)
    month_year_visited = models.DateField(null=True, blank=True)
    month_year_to_visit = models.DateField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=Trueclear)
    

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

    def __str__(self):
        return self.name

    