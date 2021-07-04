from django.shortcuts import render
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
    return render(request, 'signup.html')