from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

#create your views here
@login_required(login_url='login')
def home(request):
    username = request.user.username
    return render(request,'home.html', {'username': username})


def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['confirm_password']

        if pass1!=pass2:
            return HttpResponse("Password does not match!")
        else:   
            password=pass1
            my_user = User.objects.create_user(username,email,password)
            my_user.save()
            return redirect('login')

    return render(request,'index.html')


def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')