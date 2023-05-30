from django import forms
from .models import Destination


class DateInput(forms.DateInput):
    input_type = 'date'


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        widgets = {
            'month_year_visited': DateInput(),
            'month_year_to_visit': DateInput(),
        }
        fields = '__all__' 
        exclude = ('user',)
        # fields = ['city_name', 'country_name', 'month_year_visited', 'month_year_to_visit', 'experience_option']
