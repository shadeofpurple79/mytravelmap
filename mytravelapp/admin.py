from django.contrib import admin
from .models import Destination, Food
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'country_name', 'month_year_visited', 'month_year_to_visit', 'experience_option')
    list_filter = ('experience_option',)
    search_fields = ('city_name', 'country_name')
    date_hierarchy = 'month_year_visited'

admin.site.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination')
    list_filter = ('destination',)
    search_fields = ('name', 'destination__city_name', 'destination__country_name')
