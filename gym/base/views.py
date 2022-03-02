from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,"base/home.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["name"]
        sname = request.POST["surname"]
        email = request.POST["email"] 
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name =sname

        myuser.save()

        return redirect('signin')
        

    return render(request,"base/register.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username = username,password=pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"base/home.html",{'fname':fname})
        else:
            print('error')
            return redirect('signin')



    return render(request,"base/signin.html")

def signout(request):
    logout(request)

    return redirect('signin')


