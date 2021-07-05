from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth 
from django.contrib import messages
from django.views import generic
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Post, Comment

class HomeView(ListView):
    model = Post
    template_name = 'index.html'

class PostView(ListView):
    model = Post
    template_name = 'post.html'
    
    def post(request):
        if request.method == 'POST':
            name = request.POST['name'].capitalize()
            email = request.POST['email']
            comment = request.POST['email']

        return render(request,"post.html") 


# Create your views here.
# def index(request):
    
#     return render(request,"index.html")


def about(request):
    return render(request,"about.html")





try:
    @login_required()
    def contact(request):
        return render(request,"contact.html")
except:
    def contact(request):
        messages.info(request,'Please Login')
        return redirect('index')
    







def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Credentials!')
            return redirect('login')
    
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
@login_required()
def logout(request):
    auth.logout(request)
    return redirect('index')