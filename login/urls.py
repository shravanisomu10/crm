from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),
     path('logout/', views.logout, name='logout'),
    path('register', views.register_view, name='register_view'),
    path('do_register', views.do_register, name='do_register'),
    path('list', views.registration_data, name="list"),
   path('registration_data/', views.registration_data, name='registration_data'),
   path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
      path('users/<int:user_id>/', views.delete_user, name='delete_user'),
  # path('logout/', views.custom_logout, name='logout'), 
      
     


    #path('register/success/', views.registration_success, name='registration_success'),
]