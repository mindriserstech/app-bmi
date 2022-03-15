from atexit import register
from django.shortcuts import render
from django.http import HttpResponse

# form class import
from appbmi.form import BmiUserRegistrationForm, BmiUserLoginForm

# model class import
from appbmi.models import BmiUser, UserBmi, UserDiet

# Create your views here.

# user views
def user_index(request):
    template = 'users/index.html'
    url = 'user.login'
    content = {
        'msg': 'Welcome to BMI',
        'brand' : 'BMI',
        'page_title': 'BMI | Dashboard',
    }
    return render(request, template, content)

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
                template = 'users/index.html'
                context = {
                    'title': 'BMI | Index',
                    'msg': 'Login Success'
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
        
        umail = BmiUser.objects.get(user_email=email)
        if umail:
            context = {
                'form': rf,
                'title': 'BMI | Registration',
                'msg': 'Email already taken'
            }
            return render(request, template, context)
        else:
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