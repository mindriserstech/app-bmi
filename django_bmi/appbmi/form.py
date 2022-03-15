from django import forms
from appbmi.models import BmiUser, UserDiet, UserBmi
from django.forms import fields

class BmiUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = BmiUser
        fields = "__all__"

class BmiUserLoginForm(forms.ModelForm):
    class Meta:
        model = BmiUser
        fields = ('user_email', 'password',)

class BmiUserDietForm(forms.ModelForm):
    class Meta:
        model = UserDiet
        fields = "__all__"

class UserBmiForm(forms.ModelForm):
    class Meta:
        model = UserBmi
        fields = "__all__"