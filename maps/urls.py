from django.urls import path
from maps import views
from . import views
from .views import add_destination, destination_list



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add_destination/', add_destination, name='add_destination'),
    path('destination_list/', destination_list, name='destination_list'),
    # path('add/', views.add_destination, name='add_destination'),
    # path('destinations/', views.index, name='destination_list'),
    # path('world-map/', views.world_map, name='world_map'),
]
