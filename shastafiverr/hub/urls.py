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
    
    re_path(r'/freelancer-dashboard/', views.freelancer_dashboard, name='freelancer_dashboard'),
    
    re_path(r'/finish-job/<int:job_id>/', views.finish_job, name='finish_job'),
    
    re_path(r'/cancel-job/<int:job_id>/', views.cancel_job, name='cancel_job'),
    
    re_path(r'/accept-request/<int:job_id>/', views.accept_request, name='accept_request'),
    
    re_path(r'/decline-request/<int:job_id>/', views.decline_request, name='decline_request'),
    
    #Registration Pages
    re_path('/programming/', views.show_programming, name='cat_programming'),
    
    re_path('/graphics/', views.show_graphics, name='cat_graphics'),
    
    re_path('/video/',views.show_video, name='cat_video'),
    
    re_path('/business/', views.show_business, name='cat_business'),

    #Show Profile Pages
    re_path('register/programming/', views.show_programming, name='show_programming'),
    
    re_path('register/graphics/', views.show_graphics, name='show_graphics'),
    
    re_path('register/graphics/', views.show_video, name='show_video'),
    
    re_path('register/graphics/', views.show_business, name='show_business'),
]

