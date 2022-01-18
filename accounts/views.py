from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def home(request : WSGIRequest):
    return render(request, 'accounts/home.html')

def login(request : WSGIRequest):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {"error":"invalid username or password"})
    else:
        return render(request, 'accounts/login.html')

def logout(request : WSGIRequest):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    else:
        return render(request, 'accounts/signup.html')

def signup(request : WSGIRequest):
    if request.method == 'POST':
        if request.POST["password"] == request.POST["cpassword"]:
            try:
                user = User.objects.get(username=request.POST["username"])
                return render(request, 'accounts/signup.html', {"error":"username already taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST["username"], password = request.POST["password"])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {"error":"passwords do not match"})
    else:
        return render(request, 'accounts/signup.html')