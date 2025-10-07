from django import forms
from django.contrib.auth.models import User
from .models import Category, UserProfileInfo
from .models import ProgrammingTech, GraphicsDesign, VideoAnimation, Business
from django import forms
from .models import ClientRequest

# form function

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput()) # input for password

    class Meta():
        model = User
        fields = ('username', 'password', 'email')

class UserProfileInfoForm(forms.ModelForm):
    
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)

class BecomeFreelancerForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ['name', 'category', 'bio', 'skills', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-weight:600;'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'style':'min-height:60px; max-height:100px; resize:none; font-weight:600;'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'style':'min-height:60px; max-height:100px; resize:none; font-weight:600;'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'style':'font-weight:600;'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'style':'font-weight:600;'}),
            'category': forms.Select(attrs={'class':'form-select','style':'font-weight:600;'})       
        }

class ClientRequestForm(forms.ModelForm):
    class Meta:
        model = ClientRequest
        fields = ['email', 'details']
        widgets = {
            'details': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe what you need done'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your contact email'}),
        }

