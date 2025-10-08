from django.urls import re_path
from . import views

app_name = 'hub'

urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    
    re_path(r'^user_login/$', views.user_login, name='user_login'),
    
    re_path(r'^become-freelancer/$', views.become_freelancer, name='become_freelancer'),
    
    re_path(r'^dashboard/$', views.freelancer_dashboard, name='freelancer_dashboard'),
    
    re_path(r'^freelancer-dashboard/$', views.freelancer_dashboard, name='freelancer_dashboard'),
    
    re_path(r'^programming/$', views.show_programming, name='cat_programming'),
    
    re_path(r'^graphics/$', views.show_graphics, name='cat_graphics'),
    
    re_path(r'^video/$', views.show_video, name='cat_video'),
    
    re_path(r'^business/$', views.show_business, name='cat_business'),

    re_path(r'^freelancer/hire/(?P<freelancer_id>\d+)/$', views.hire_freelancer, name='hire_freelancer'),
    
    re_path(r'^freelancer/view/(?P<freelancer_id>\d+)/$', views.view_freelancer, name='view_freelancer'),

    re_path(r'^freelancer/request/(?P<request_id>\d+)/$', views.view_request, name='view_request'),
    
    re_path(r'^freelancer/job/(?P<request_id>\d+)/finish/$', views.finish_job, name='finish_job'),
    
    re_path(r'^freelancer/job/(?P<request_id>\d+)/cancel/$', views.cancel_job, name='cancel_job'),

    re_path(r'^freelancer/request/(?P<request_id>\d+)/accept/$', views.accept_request, name='accept_request'),
    
    re_path(r'^freelancer/request/(?P<request_id>\d+)/decline/$', views.decline_request, name='decline_request'),
]