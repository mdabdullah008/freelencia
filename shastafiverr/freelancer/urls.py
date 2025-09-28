from freelancer import views
from django.urls import re_path
app_name = 'freelancer'

urlpatterns = [
	re_path(r'register/', views.register, name='register'),

	re_path(r'user_login/', views.user_login, name='user_login'),
]



 