from unicodedata import category
from django.shortcuts import redirect, render, get_object_or_404
from .forms import BecomeFreelancerForm, UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import UserProfileInfo, ClientRequest, User
from django.core.mail import send_mail
from django.conf import settings


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
    profile = request.user.userprofileinfo

    # Accepted jobs → show in Client List
    client_list = request.user.received_requests.filter(status='accepted')
    
    # Pending requests → show in Client Requests
    client_requests = request.user.received_requests.filter(status='pending')

    context = {
        'profile': profile,
        'client_list': client_list,
        'client_requests': client_requests,
        }
    
    return render(request, 'hub/freelancer_dashboard.html', context)


@login_required
def finish_job(request, request_id):
    
    # Optional: mark job as finished (could add a 'finished' status)
    
    client_request = get_object_or_404(ClientRequest, id=request_id, freelancer=request.user)
    client_request.status = 'finished'
    client_request.save()

    send_mail(
    subject="Your job has been marked as completed!",
    message=f"Hello {client_request.client.username},\n\n"
            f"{request.user.username} has marked your job as finished.\n\n"
            f"Thank you for using Freelencia!",
    from_email=settings.DEFAULT_FROM_EMAIL,
    recipient_list=[client_request.email],
)
    
    return redirect('hub:freelancer_dashboard')


@login_required
def cancel_job(request, request_id):
    
    client_request = get_object_or_404(ClientRequest, id=request_id, freelancer=request.user)
    client_request.status = 'cancelled'
    client_request.save()
    
    send_mail(
    subject="Your job has been cancelled!",
    message=f"Hello {client_request.client.username},\n\n"
            f"{request.user.username} has cancelled your job.\n\n"
            f"Thank you for using Freelencia!",
    from_email=settings.DEFAULT_FROM_EMAIL,
    recipient_list=[client_request.email],
)
    
    return redirect('hub:freelancer_dashboard')



@login_required
def accept_request(request, request_id):
    
    client_request = get_object_or_404(ClientRequest, id=request_id, freelancer=request.user)
    client_request.status = 'accepted'
    client_request.save()

    # Send email to client confirming acceptance
    
    send_mail(
        subject="Your job request has been accepted!",
        message=f"Hello {client_request.client.username},\n\n"
                
                f"{request.user.username} has accepted your request.\n\n"
                
                f"Job Details: {client_request.details}\n"
                
                f"Contact Email: {client_request.email}\n\n"
                
                f"Please communicate with the freelancer via email.",
        
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[client_request.email],
        )

    return redirect('hub:freelancer_dashboard')



@login_required
def decline_request(request, request_id):
    
    client_request = get_object_or_404(ClientRequest, id=request_id, freelancer=request.user)
    client_request.status = 'cancelled'
    client_request.save()

    send_mail(
    subject="Your job has been declined.",
    message=f"Hello {client_request.client.username},\n\n"
            f"{request.user.username} has declined your job.\n\n"
            f"Thank you for using Freelencia!",
    from_email=settings.DEFAULT_FROM_EMAIL,
    recipient_list=[client_request.email],
)
    
    return redirect('hub:freelancer_dashboard')


def show_programming(request):
    profiles = UserProfileInfo.objects.filter(category__name='Programming and Tech', role='freelancer')
    
    return render(request, 'hub/show_table.html', {
        'profiles': profiles,
        'category_name': 'Programming and Tech'
    })


def show_graphics(request):
    profiles = UserProfileInfo.objects.filter(category__name='Graphics and Design', role='freelancer')
    
    return render(request, 'hub/show_table.html', {'profiles': profiles, 'category_name': 'Graphics and Design'})


def show_video(request):
    profiles = UserProfileInfo.objects.filter(category__name='Video and Animation', role='freelancer')
    
    return render(request, 'hub/show_table.html', {'profiles': profiles, 'category_name': 'Video and Animation'})



def show_business(request):
    profiles = UserProfileInfo.objects.filter(category__name='Business', role='freelancer')
    return render(request, 'hub/show_table.html', {'profiles': profiles, 'category_name': 'Business'})



@login_required
def hire_freelancer(request, freelancer_id):
    from .forms import ClientRequestForm
    freelancer = get_object_or_404(User, id=freelancer_id)

    if request.method == "POST":
        form = ClientRequestForm(request.POST)
        if form.is_valid():
            client_request = form.save(commit=False)
            client_request.freelancer = freelancer
            client_request.client = request.user
            client_request.save()

            profile = UserProfileInfo.objects.get(user=freelancer)
            send_mail(
                subject=f"New Job Request from {request.user.username}",
                message=f"Job Details: {client_request.details}\n"
                        f"Contact Email: {client_request.email}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[profile.email],
                
            )
            return redirect('hub:hired_freelancer_profile', freelancer_id=freelancer.id)
    else:
        form = ClientRequestForm()

    return render(request, 'hub/hire_freelancer.html', {'form': form, 'freelancer': freelancer})

@login_required
def view_request(request, request_id):
    
    client_request = get_object_or_404(ClientRequest, id=request_id, freelancer=request.user)

    return render(request, "hub/view_request.html", {
        "request_obj": client_request
    })

@login_required
def view_freelancer(request, freelancer_id):
    freelancer = get_object_or_404(UserProfileInfo, id=freelancer_id)

    return render(request, "hub/view_freelancer.html", {
        "freelancer": freelancer,
        "category": category
    })

from .models import ClientRequest

@login_required
def hired_freelancers(request):
    hires = ClientRequest.objects.filter(client=request.user)
    return render(request, 'hub/hired_freelancers.html', {'hires': hires})

@login_required
def hired_freelancer_profile(request, freelancer_id):
    client_request = ClientRequest.objects.filter(client=request.user, freelancer_id=freelancer_id).first()
    if not client_request:
        return HttpResponseForbidden("You did not hire this freelancer.")

    freelancer = client_request.freelancer

   
    profile = getattr(freelancer, 'userprofileinfo', None)

    return render(request, 'hub/hired_freelancer_profile.html', {
        'freelancer': freelancer,
        'hire': client_request, 
        'profile': profile       
    })

@login_required
def view_client_request(request, request_id):

    client_request = get_object_or_404(ClientRequest, id=request_id, freelancer=request.user)
    return render(request, 'hub/view_client_request.html', {'request_obj': client_request})


@login_required
def view_hired_client(request, request_id):

    client_request = get_object_or_404(ClientRequest, id=request_id, freelancer=request.user)
    return render(request, 'hub/view_hired_client.html', {'request_obj': client_request})