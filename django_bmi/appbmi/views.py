from atexit import register
from cgitb import reset
import email
from re import sub, template
from winreg import REG_QWORD
from django.shortcuts import redirect, render
from django.http import HttpResponse

# importing email classes
from django.core.mail import send_mail
from django.conf import settings

# form class import
from appbmi.form import BmiUserRegistrationForm, BmiUserLoginForm, BmiUserProfileForm

# model class import
from appbmi.models import BmiUser, UserBmi, UserDiet
from appbmi.form import UserBmiForm

# Create your views here.

# bmi views
def bmi_index(request):
    template = 'userbmi/index.html'
    bmi = UserBmi.objects.all()
    context = {
        'data': bmi,
        'page_title': 'BMI Calculate',
        'brand': 'BMI'
    }
    return render(request, template, context)

def bmi_create(request):
    template = 'userbmi/create.html'
    bmiform = UserBmiForm
    context = {
        'page_title': 'BMI Record',
        'form': bmiform,
        'brand': 'BMI'
    }
    return render(request, template, context)

def bmi_store(request):
    if request.method == "POST":
        bmi = UserBmi()
        bmi.weight = request.POST.get('weight')
        bmi.height = request.POST.get('height')
        bmi.bmi_unit = request.POST.get('bmi_unit')
        bmi.bmi = request.POST.get('bmi')
        bmi.user_id = request.POST.get('user_id')
        bmi.save()
        template = 'userbmi/index.html'
        bmi_data = UserBmi.objects.all()
        context = {
            'data': bmi_data,
            'page_title': 'BMI Calculate',
            'brand': 'BMI'
        }
        return render(request, template, context)
    else:
        template = 'userbmi/create.html'
        bmiform = UserBmiForm
        context = {
            'page_title': 'BMI Record',
            'form': bmiform,
            'brand': 'BMI'
        }
        return render(request, template, context)


def bmi_edit(request, bmi_id):
    template = 'userbmi/edit.html'
    bmiuser = UserBmi.objects.get(id=bmi_id)
    context = {
        'page_title': 'BMI Edit',
        'data': bmiuser,
        'brand': 'BMI'
    }
    return render(request, template, context)

def bmi_update(request):
    if request.method == "POST":
        bmi = UserBmi.objects.get(id=request.POST.get('id'))
        bmi.weight = request.POST.get('weight')
        bmi.height = request.POST.get('height')
        bmi.bmi_unit = request.POST.get('bmi_unit')
        bmi.bmi = request.POST.get('bmi')
        bmi.user_id = request.POST.get('user_id')
        bmi.save()
        template = 'userbmi/index.html'
        bmi_data = UserBmi.objects.all()
        context = {
            'data': bmi_data,
            'page_title': 'BMI Calculate',
            'brand': 'BMI'
        }
        return render(request, template, context)
    else:
        template = 'userbmi/index.html'
        bmiform = UserBmiForm
        context = {
            'page_title': 'BMI Record List',
            'form': bmiform,
            'brand': 'BMI'
        }
        return render(request, template, context)

def bmi_delete(request, bmi_id):
    userbmi = UserBmi.objects.get(id=bmi_id)
    userbmi.delete()
    bmi_data = UserBmi.objects.all()
    template = 'userbmi/index.html'
    context = {
        'page_title': 'BMI Record List',
        'brand': 'BMI',
        'data': bmi_data
    }
    return render(request, template, context)

def bmi_show(request, bmi_id):
    userbmi = UserBmi.objects.get(id=bmi_id)
    template = 'userbmi/show.html'
    context = {
        'page_title': 'BMI Show',
        'brand': 'BMI',
        'data': userbmi
    }
    return render(request, template, context)

# user views
# email send
def sendemail(request):

    # post method
    # subject = request.POST.get('subject')
    # message = request.POST.get('message')
    
    subject = 'TEST DEMO of SEND EMAIL'
    message = 'This is a peaceful country'
    email_from = settings.EMAIL_HOST_USER
    recepient_list = ['izvirzl@gmail.com']

    send_mail(subject, message, email_from, recepient_list)

    return redirect('users/index')

def user_profile_upload(request):
    user = BmiUser.objects.get(user_email=request.session['session_email'])
    template = 'users/show.html'
    pf = BmiUserProfileForm
    if request.method == "POST":
        form = BmiUserProfileForm(request.POST, request.FILES)
        user = BmiUser.objects.get(user_email=request.session['session_email'])
        if form.is_valid():
            form.save()
            context = {
                'page_title': 'BMI | User Profile',
                'brand': 'BMI',
                'data': user,
                'profile_form': pf,
                'msg_pf_success': 'Uploaded successfully'
            }
            return render(request, template, context)
    else:
        context = {
            'page_title': 'BMI | User Profile',
            'brand': 'BMI',
            'data': user,
            'profile_form': pf,
            'msg_pf_error': 'Something went wrong'
        }
        return render(request, template, context)

def user_index(request):
    if request.session.has_key('session_email'):
        user = BmiUser.objects.get(user_email=request.session['session_email'])
        template = 'users/index.html'
        context = {
            'page_title': 'BMI | Index',
            'brand': 'BMI',
            'data': user
        }
        return render(request, template, context)
    else:
        template = 'users/login.html'
        ul = BmiUserLoginForm()
        context = {
            'form': ul,
            'title': 'BMI | Login',
            'msg': 'Acess Forbidden'
        }
        return render(request, template, context)

def user_logout(request):
    del request.session['session_email']
    template = 'users/login.html'
    ul = BmiUserLoginForm()
    context = {
        'form': ul,
        'title': 'BMI | Login',
        'msg_success': 'Logout Success'
    }
    return render(request, template, context)

def user_profile(request):
    if request.session.has_key('session_email'):
        user = BmiUser.objects.get(user_email=request.session['session_email'])
        template = 'users/show.html'
        pf = BmiUserProfileForm
        context = {
            'page_title': 'BMI | User Profile',
            'brand': 'BMI',
            'data': user,
            'profile_form': pf
        }
        return render(request, template, context)
    else:
        template = 'users/login.html'
        ul = BmiUserLoginForm()
        context = {
            'form': ul,
            'title': 'BMI | Login',
            'msg': 'Email or password invalid'
        }
        return render()

def user_update(request):
    template = 'users/show.html'

    if request.method == "POST":
        user = BmiUser.objects.get(user_email=request.session['session_email'])
        user.first_name = request.POST.get('first_name')
        user.middle_name = request.POST.get('middle_name')
        user.last_name = request.POST.get('last_name')
        user.user_email = request.POST.get('user_email')
        user.username = request.POST.get('username')
        user.save()
        context = {
            'page_title': 'BMI | User Profile',
            'brand': 'BMI',
            'data': user,
            'msg_success': 'Updated successfully'
        }
        return render(request, template, context)
    else:
        context = {
            'page_title': 'BMI | User Profile',
            'brand': 'BMI',
            'data': user,
            'msg_error': 'Something went wrong'
        }
        return render(request, template, context)

def user_login(request):
    template = 'users/login.html'
    ul = BmiUserLoginForm()
    if request.method == "POST":
        # method one
        # email = request.POST['user_email']
        # method two 
        email = request.POST.get('user_email')
        password = request.POST.get('password')
        try:
            user = BmiUser.objects.get(user_email=email)
            if password == user.password:
                # storing session
                request.session['session_email'] = user.user_email

                # checking session 
                if request.session.has_key('session_email'):
                    template = 'users/index.html'
                    context = {
                        'page_title': 'BMI | Index',
                        'brand': 'BMI',
                        'data': user
                    }
                    return render(request, template, context)
                else:
                    context = {
                        'form': ul,
                        'title': 'BMI | Login',
                        'msg': 'Email or password invalid'
                    }
                    return render(request, template, context)
            else:
                context = {
                    'form': ul,
                    'title': 'BMI | Login',
                    'msg': 'Email or password invalid'
                }
                return render(request, template, context)
        except:
            context = {
                'form': ul,
                'title': 'BMI | Login',
                'msg': 'Something went wrong'
            }
            return render(request, template, context)
    else:
        context = {
            'form': ul,
            'title': 'BMI | Login',
            'msg': ''
        }
        return render(request, template, context)

def user_create(request):
    template = 'users/create.html'
    rf = BmiUserRegistrationForm
    context = {
        'form': rf,
        'title': 'BMI | Registration'
    }
    if request.method == "POST":
        fname = request.POST.get('first_name')
        mname = request.POST.get('middle_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('user_email')
        uname = request.POST.get('username')
        passwd = request.POST.get('password')
        
        try:
            umail = BmiUser.objects.get(user_email=email)
            if umail:
                context = {
                    'form': rf,
                    'title': 'BMI | Registration',
                    'msg': 'Email already taken'
                }
            return render(request, template, context)
        except:
            # to store data in database
            try:
                user = BmiUser()
                user.first_name = fname
                user.middle_name = mname
                user.last_name = lname
                user.user_email = email
                user.username = uname
                user.password = passwd
                user.save()
                ul = BmiUserLoginForm()
                context = {
                    'title': 'BMI | Login',
                    'msg_success': 'Registration Success',
                    'form': ul
                }
                template = 'users/login.html'
                return render(request, template, context)
            except:
                context = {
                    'form': rf,
                    'title': 'BMI | Registration',
                    'msg': 'Something went wrong'
                }
                return render(request, template, context)
    else:
        return render(request, template, context)