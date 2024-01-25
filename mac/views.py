from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.


def register(request):
     if request.method == 'POST':
          username = request.POST['username']
          email = request.POST['email']
          password1 = request.POST['password1']
          password2 = request.POST['password2']
          if password1 == password2:
               if User.objects.filter(username=username).exists():
                    messages.success(request, 'User already exit')
                    return redirect('/')
               elif User.objects.filter(email=email).exists():
                    messages.success(request, 'Email already exits')
                    return redirect('/')
               else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()

          else:
               messages.warning(request, 'password is not correct')
               return redirect('/')

     return render(request,'register.html')

def login(request):

  if request.method == 'POST':
     username = request.POST['username']
     password = request.POST['password']
     login_user = auth.authenticate(username=username,password=password)
     if login_user is not None:
        auth.login(request,login_user)
        messages.info(request,'successfully login')
        return redirect('/shop')
     else:
        messages.info(request,'user is not exits')
  return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/login')
