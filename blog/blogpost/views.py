from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User , auth 
from django.contrib import messages
from django.views import generic
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from django.urls import reverse_lazy, reverse 
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

class HomeView(ListView):
    model = Post
    template_name = 'index.html'






def posts(request,slug):
    
    if request.method != 'POST':
        posts = Post.objects.get(slug = slug)
    elif request.method == 'POST':
        post_instance = get_object_or_404(Post, slug=slug)
        name = request.POST['name']
        email = request.POST['email']
        comment_body = request.POST['comment']
        post = Comment()
        post.name = name
        post.post = post_instance
        post.email = email
        post.body = comment_body
        post.save()
        return redirect('post',slug=slug)
        
    else:
        pass
    return render(request,"post.html",{'post':posts}) 









# Create your views here.
# def index(request):
    
#     return render(request,"index.html")


def about(request):
    return render(request,"about.html")





# @login_required_message(message="You should be logged in to make conatact.")
@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
        name,
        message,
        email,
        ['kalyani2007shinde@gmail.com'],
        fail_silently=False,)
        messages.info(request,'Message sent succesfully!')
        return redirect('contact')


    else:
        return render(request,"contact.html")

    







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



@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('index')



# def LikeView(request,slug):
#     post_like = get_object_or_404(Post, slug=slug)
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('HomeView',args=[str(slug)]))
