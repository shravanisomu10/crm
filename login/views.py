from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
#from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout



def home(request):
    return render(request, 'home.html')
def index(request):
    return render(request, "login/index.html")

def register_view(request):
    return render(request, "register/registration.html")  

def do_register(request):
    #eturn HttpResponse(request.POST, content_type='text/plain')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password'] 
        encrypted_password = make_password(password)
        user = User(first_name=first_name, last_name=last_name,email=email,password=encrypted_password,username=username)
        user.save()

        messages.success(request, 'Registration successful')
        user = authenticate(request, email=email, password=password)
        if user is not None:
           
            messages.success(request, 'Registration and Login successful')
        else:
            messages.error(request, 'Error occurred during registration')

        return redirect('register_view')
    else:
        return redirect('register_view')

@login_required(login_url="/login/")
def registration_data(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'register/registration_data.html', context)

@login_required(login_url="/login/")
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    #print(user.password)
    context = {'user': user}
    return render(request, 'login/edit_user.html', context)

def update_user(request, user_id):
    #return HttpResponse(user_id, content_type='text/plain')
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        user.first_name = request.POST['first_name']
        user.username = request.POST['username']
        user.last_name = request.POST['last_name']
        user.password = request.POST['password']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.address = request.POST['address']
        user.save()

        messages.success(request, 'User details updated successfully')

        return redirect('registration_data')
    else:
        return redirect('registration_data')
    
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('registration_data')

def login_user(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
      
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            #return HttpResponse(user.is_authenticated, content_type='text/plain')
            #auth_login(request, user) 
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('list')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, "login/login.html")
def logout(request):
    auth_logout(request)
    return redirect('login') 
