from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.views import generic
from .models import Post

# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request,"index.html",{'post':post})


def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")


def post(request,pk):
    posts = Post.objects.get(id = pk)
    return render(request,"post.html",{'post':posts}) 

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        first_name =  request.POST['first_name'].capitalize()
        last_name = request.POST['last_name'].capitalize()
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email Already Used')
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username Already Used')
            return redirect('signup')
        else:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
            user.save()
            messages.info(request,'Account Created Succesfully!')
            return redirect('login')
        

    return render(request, 'signup.html') 