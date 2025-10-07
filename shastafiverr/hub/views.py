from django.shortcuts import redirect, render, get_object_or_404
from .forms import BecomeFreelancerForm, UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Job, UserProfileInfo
from .forms import ProgrammingTechForm, GraphicsDesignForm, VideoAnimationForm, BusinessForm
from .models import ProgrammingTech, GraphicsDesign, VideoAnimation, Business

# Create your views here.

def index(request):
    return render(request, 'hub/index.html')

@login_required
def special(request):
    return HttpResponse("You are now logged in")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.role = 'customer'
            if 'profile_pic' in request.FILES:
                print('Got it...')
                profile.profile_pic = request.FILES['profile_pic']
            else:
                pass
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    return render(request, 'hub/registration.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active: 
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Sorry, your account is inactive.")
        else:
            return render(request, 'hub/login.html', {
                'error': "Invalid username or password, Please try again."
            })
    else:
        return render(request, 'hub/login.html', {})

@login_required
def become_freelancer(request):
    profile = request.user.userprofileinfo

    if request.method == 'POST':
        form = BecomeFreelancerForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.role = 'freelancer'
            profile.save()
            form.save_m2m()
            return redirect('hub:freelancer_dashboard')
    else:
        form = BecomeFreelancerForm(instance=profile)

    return render(request, 'hub/become_freelancer.html', {'form': form})

@login_required
def freelancer_dashboard(request):
    user = request.user
    try:
        profile = UserProfileInfo.objects.get(user=user)
    except UserProfileInfo.DoesNotExist:
        profile = None
        
    client_list = Job.objects.filter(freelancer=user).exclude(status='requested')
    client_requests = Job.objects.filter(freelancer=user).exclude(status='requested')
    
    return render(request, 'hub/freelancer_dashboard.html', {
                  'user' : user,
                  'profile' : profile,
                  'client_list' : client_list,
                  'client_requests' : client_requests,
                  })

@login_required
def finish_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, freelancer=request.user)
    job.status = 'done'
    job.save()
    return redirect('hub:freelancer_dashboard')

@login_required
def cancel_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, freelancer=request.user)
    job.status = 'cancelled'
    job.save()
    return redirect('hub:freelancer_dashboard')

@login_required
def accept_request(request, job_id):
    job = get_object_or_404(Job, id=job_id, freelancer=request.user)
    job.status = 'ongoing'
    job.save()
    return redirect('hub:freelancer_dashboard')

@login_required
def decline_request(request, job_id):
    job = get_object_or_404(Job, id=job_id, freelancer=request.user)
    job.status = 'cancelled'
    job.save()
    return redirect('hub:freelancer_dashboard')

def show_programming(request):
    profiles = UserProfileInfo.objects.filter(category__name='Programming and Tech', role='freelancer')
    return render(request, 'hub/show_table.html', {
        'profiles': profiles,
        'category_name': 'Programming and Tech'
    })

def show_graphics(request):
    profiles = UserProfileInfo.objects.filter(category__name='Graphics')
    return render(request, 'hub/show_table.html', {'profiles': profiles, 'category_name': 'Graphics and Design'})

def show_video(request):
    profiles = UserProfileInfo.objects.filter(category__name='Video')
    return render(request, 'hub/show_table.html', {'profiles': profiles, 'category_name': 'Video and Animation'})

def show_business(request):
    profiles = UserProfileInfo.objects.filter(category__name='Business')
    return render(request, 'hub/show_table.html', {'profiles': profiles, 'category_name': 'Business'})

