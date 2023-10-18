from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),

    path('details/<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('edit/<int:pk>', views.ticket_edit, name='ticket_edit'),
    path('delete/<int:pk>', views.ticket_delete, name='ticket_delete'),
    path('new/', views.ticket_new, name='ticket_new'),
      
  
    
]
