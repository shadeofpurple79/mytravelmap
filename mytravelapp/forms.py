from django import forms
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'
        # fields = ['city_name', 'country_name', 'month_year_visited', 'month_year_to_visit', 'experience_option']