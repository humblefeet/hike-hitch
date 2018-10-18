from django.urls import path, include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name ='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('trails/', views.trails_index, name='trails_index'),
    path('trails/<int:trail_id>', views.trails_detail, name="trails_detail"),
    path('trails/create/', views.TrailCreate.as_view(), name='trail_create'),
    path('logout/', views.logout_view, name="logout_view"),
    path('user/<username>', views.profile, name ='profile'),
    path('hiker/<int:pk>/update/', views.HikerUpdate.as_view(), name='hiker_update'),
    path('hikers/', views.hikers_index, name='hikers_index'),
    path('signup/hikers/create/', views.HikerCreate.as_view(), name='hiker_create'),
    path('trips/', views.trips, name='trips'),
    path('trips/create/', views.TripCreate.as_view(), name='trip_create'),
    path('trips/<int:pk>/delete/', views.TripsDelete.as_view(), name="trips_delete"),
    path('trips/<int:trip_id>', views.trips_detail, name="trips_detail"),
    path('wish/',views.wish, name="wish"),
]