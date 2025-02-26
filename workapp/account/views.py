from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "account/login.html")

def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", 
                {
                    "error": "Username already exists",
                    "username": username,
                    "email": email,
                    "firstname": first_name,  
                    "lastname": last_name,
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html",
                    {
                        "error": "Email already exists",
                        "username": username,
                        "email": email,
                        "firstname": first_name,  
                        "lastname": last_name,
                    })
                       
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        first_name=first_name, 
                        last_name=last_name, 
                        password=password
                        )
                    user.save()
                    return redirect("login")
        else:
            return render(request, "account/register.html", {
                "error": "Passwords do not match",
                "username": username,
                "email": email,
                "firstname": first_name,  
                "lastname": last_name,
                })
            


    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("home")
