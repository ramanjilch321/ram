from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def signup_views(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        email = request.POST['email']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username not available')
                return render(request,'signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is taken')
                return render(request,'signup.html')
                
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return render(request,'signin.html')
        else:
            messages.info(request,'password mismatch')
            return render(request,'signup.html')
        
        
    else:
        return render(request,'signup.html')




def signin_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,'login success')
            return render(request,'index.html')
        else:
            messages.info(request,'invalid credientials')
            return render(request,'signin.html')
    else:
        return render(request,'signin.html')


def logout_views(request):
    auth.logout(request)
    return redirect('/')



def index_views(request):
    return render(request,'index.html')



def about_views(request):
    return render(request,'about.html')


def contact_views(request):
    return render(request,'contact.html')

def services_views(request):
    return render(request,'services.html')