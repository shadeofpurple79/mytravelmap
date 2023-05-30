from django.urls import path
from maps import views
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('add/', views.add_destination, name='add_destination'),
    # path('destinations/', views.index, name='destination_list'),
    # path('world-map/', views.world_map, name='world_map'),
]
