from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('trails/', views.trails_index, name='trails_index'),
    path('trails/<int:trail_id>', views.trails_detail, name="trails_detail"),
    path('logout/', views.logout_view, name="logout_view"),

]