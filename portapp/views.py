from urllib import request
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from portapp.models import *
from portapp.forms import *
from django.contrib import messages
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'portapp/blog.html', {'blog':blog})

# def blog_detail(request):
#     return render(request, 'portapp/blog_detail.html') 
# class BlogDetail(DetailView):
#     model =Blog
#     template_name = 'portapp/blog_detail.html' 
#     context_object_name = 'blog_detail' 

def BlogDetail(request, pk):
    blog_detail = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(post__pk=pk).order_by('-created')
    most_recent = Blog.objects.order_by()[:3]
    if request.method == 'POST':
        comm = CommentForm(request.POST, request.FILES)
        if comm.is_valid():
            new_comment = comm.save(commit=False)
            new_comment.post = blog_detail
            new_comment.save()
            return redirect('portapp:blog_detail', pk=blog_detail.pk)
    else:
        comm = CommentForm()
   

    return render(request, 'portapp/blog_detail.html', {'comm':comm, 'comments':comments,'blog_detail':blog_detail, 'most_recent':most_recent})
     

    
def index(request):
    education = Education.objects.all()
    if request.method =="POST":
        cform = ContactForm(request.POST)
        if cform.is_valid():
            cform.save()
    else:
        cform = ContactForm()        
    return render(request, 'portapp/home.html', {'education':education, 'cform':cform})

def regform(request):
    if request.method =='POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request, 'successfully created')
            return redirect('portapp:login')
    else:
        form = RegForm()
        
    return render(request,'portapp/reg.html', {'reg':form})     

def login_user (request):
    if request.method=='POST':
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')  
            messages.info(request, f'welcome to the dashboard {{user.username}}')     
    else:
        return render (request, 'portapp/login.html')





        



