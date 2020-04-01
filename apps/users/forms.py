from django import forms
from allauth.account.forms import SignupForm
from .models import User, UserProfile


class UserEditForm(forms.ModelForm):

    #def __init__(self, *args, **kwargs):
        # TODO: this doesn't seem to work. Need to get to the bottom of it.
    #    super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'display_name')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', "email_private", 'first_name_private', 'last_name_private']

class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'display_name', 'is_staff', 'is_active', 'date_joined')

    def is_valid(self):
        return super().is_valid()


YEARS= [x for x in range(1940,2021)]

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=26, label='First name')
    last_name = forms.CharField(max_length=26, label='Last name')
    display_name = forms.CharField(max_length=14, label='Display name')
    dob = forms.CharField(label='Date of Birth', widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'display_name', 'dob')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.display_name = self.cleaned_data['display_name']    
        user.dob = self.cleaned_data['dob']    
        user.save()
        return user

