from hub import views
from django.urls import re_path
from django.urls import path
from . import views

app_name = 'hub'

urlpatterns = [
	re_path(r'/register/', views.register, name='register'),

	re_path(r'/user_login/', views.user_login, name='user_login'),
    
    re_path(r'/become-freelancer/', views.become_freelancer, name='become_freelancer'),
    
	re_path(r'/dashboard/', views.freelancer_dashboard, name="freelancer_dashboard"),
    
    path('freelancer-dashboard/', views.freelancer_dashboard, name='freelancer_dashboard'),
    
    path('finish-job/<int:job_id>/', views.finish_job, name='finish_job'),
    
    path('cancel-job/<int:job_id>/', views.cancel_job, name='cancel_job'),
    
    path('accept-request/<int:job_id>/', views.accept_request, name='accept_request'),
    
    path('decline-request/<int:job_id>/', views.decline_request, name='decline_request'),

]

