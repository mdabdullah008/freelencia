from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps

def role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if request.user.userprofileinfo.role !=required_role:
                return HttpResponse("Access Denied. Only %s can see this page" % required_role)
            return view_func(request, *args, **kwargs)
        return decorator
    
freelancer_required = role_required('freelancer')
customer_required = role_required('customer')