from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('events/', views.events, name='events'),
    path('delete/<event_id>', views.delete, name='delete'),
    path('ticket/<event_id>', views.ticket, name='ticket'),
    path('payment/<event_id>', views.payment, name='payment'),
    ]