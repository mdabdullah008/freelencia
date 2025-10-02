from freelancer import views
from django.urls import re_path
from django.urls import path
from . import views
app_name = 'freelancer'

urlpatterns = [
	re_path(r'register/', views.register, name='register'),

	re_path(r'user_login/', views.user_login, name='user_login'),

	path('register/', views.register, name='register'),
    
    path('become-freelancer/', views.become_freelancer, name='become_freelancer'),
    
    path('dashboard/customer/', views.customer_dashboard, name='customer_dashboard'),
    
    path('dashboard/freelancer/', views.freelancer_dashboard, name='freelancer_dashboard'),
]




