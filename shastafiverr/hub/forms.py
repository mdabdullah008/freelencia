from django import forms
from django.contrib.auth.models import User
from .models import Category, UserProfileInfo

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
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = UserProfileInfo
        fields = ['name', 'categories', 'bio', 'skills']

