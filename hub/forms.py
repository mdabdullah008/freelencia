from django import forms
from django.contrib.auth.models import User
from .models import Category, UserProfileInfo
from .models import ProgrammingTech, GraphicsDesign, VideoAnimation, Business

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

class ProgrammingTechForm(forms.ModelForm):
    class Meta:
        model = ProgrammingTech
        fields = ['name', 'profile_pic', 'email', 'age', 'education']

class GraphicsDesignForm(forms.ModelForm):
    class Meta:
        model = GraphicsDesign
        fields = ['name', 'profile_pic', 'email', 'age', 'education']
            
class VideoAnimationForm(forms.ModelForm):
    class Meta:
        model = VideoAnimation
        fields = ['name', 'profile_pic', 'email', 'age', 'education']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'profile_pic', 'email', 'age', 'education']

