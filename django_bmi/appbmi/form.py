from django import forms
from appbmi.models import BmiUser, UserDiet, UserBmi
from django.forms import fields

class BmiUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = BmiUser
        fields = ('first_name','middle_name','last_name','username','user_email', 'password',)

class BmiUserLoginForm(forms.ModelForm):
    class Meta:
        model = BmiUser
        fields = ('user_email', 'password',)

class BmiUserProfileForm(forms.ModelForm):
    class Meta:
        model = BmiUser
        fields = ('profile_url',)

class BmiUserDietForm(forms.ModelForm):
    class Meta:
        model = UserDiet
        fields = "__all__"

class UserBmiForm(forms.ModelForm):
    class Meta:
        model = UserBmi
        fields = "__all__"