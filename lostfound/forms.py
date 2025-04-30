from datetime import datetime, timedelta

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils import timezone

from . models import CustomUser, Item, claimRequestReport, fraudClaimReport


#User Creation
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required= True)
    
    class Meta:
        model = CustomUser
        fields = ('username','email','first_name','last_name','password1','password2')

#User password change
class CustomUserChangeForm(UserChangeForm):
       
    class Meta:
        model = CustomUser
        fields = ("username","email","first_name","last_name","password")
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': "Enter email"}),
            'first_name': forms.TextInput(attrs={'placeholder': "First Name"}),
            'last_name' : forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'password' : forms.PasswordInput(attrs={'placeholder': ""})
        }
    

# Item Creation:
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'itemName',
            'description',
            'category',
            'location',
            'photo',
            'status',
            'contactInfo',
            'sensitiveItem',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # The following are optional:
        self.fields['photo'].required = False
        self.fields['description'].required = False

    def save(self, commit=True):
        instance = super().save(commit = False)
        dateToExpire = timezone.now() + timedelta(weeks=1)
        instance.dateToExpire = dateToExpire
        if commit:
            instance.save()
        return instance
        

# Claims creation:
class claimForm(forms.ModelForm):
    class Meta:
        model = claimRequestReport
        fields = ['proofOfOwnership']
        widgets = {
            'proofOfOwnership': forms.Textarea(attrs={'rows':3, 'placeholder': 'Please describe the item in detail.'}),
        }

# Fraud creation:
class fraudForm(forms.ModelForm):
    class Meta:
        model = fraudClaimReport
        fields = ['contactInfo','proofOfOwnership',]
        widgets = {
            'proofOfOwnership': forms.Textarea(attrs={'rows':3, 'placeholder': 'Please describe the why this item is yours.'}),
        }


class searchForm(forms.Form):
    query = forms.CharField(max_length=255, required= True, label="Search")



