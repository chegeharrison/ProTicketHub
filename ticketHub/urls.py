from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('events/', views.events, name='events'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('testing/', views.testing, name='testing'),

]
