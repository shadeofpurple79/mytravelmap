from django.urls import path
from mytravelapp import views
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('world-map/', views.world_map, name='world_map'),
]
