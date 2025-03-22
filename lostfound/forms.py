from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username","email")

class searchForm(forms.Form):
    query = forms.CharField(max_length=255, required= True, label="Search")

class claimItemForm(forms.Form):
    proofDescription = forms.CharField(widget=forms.Textarea,required=True, label= "Please describe the item in detail.")