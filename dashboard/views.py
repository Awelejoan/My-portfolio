from django.shortcuts import render, redirect,get_object_or_404
from dashboard.forms import *
from portapp.models import Blog
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def dash(request):
    return render(request, 'dashboard/dashboard.html')
def log(request):
    return render(request,'dashboard/login.html') 
def addblog(request):
    if request.method=='POST':
        blog = AddBlog(request.POST, request.FILES)
        if blog.is_valid():
            blog.save()
            return redirect('dashboard:viewblog')
            messages.success(request,'Blog posted')
            
    else:
        blog = AddBlog()
    return render(request, 'dashboard/addblog.html', {'Blog':blog}) 

def passwordview(request):
    if request.method=='POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully')
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'dashboard/changepassword.html', {'form_key':form})


def profilepage(request):
    return render(request, 'dashboard/profile.html')        
    
def edit_profile(request):
    if request.method=='POST':
        p_form = EditUserForm(request.POST, instance=request.user)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'your account has been updated!')
            # return redirect('dashboard:profile')
    else:
        p_form = EditUserForm(instance=request.user)
    
    context ={
        'p_form':p_form
    }             
    return render(request, 'dashboard/editprofile.html',context)

# @login_required(login_url='user:login')
def viewblog(request):
    view_blog = Blog.objects.filter(poster=request.user)
    return render(request, 'dashboard/viewblog.html', {'view':view_blog})  
         
# for the view blog of the dashboard i.e edit,delete and view
def edit_post(request, pk):
    editblog =get_object_or_404(Blog, pk=pk)
    if request.method =='POST':
        editblog = EditBlogForm(request.POST, request.FILES, instance=editblog)
        if editblog.is_valid():
            editblog.save()
            return redirect('dashboard:viewblog') 
            mesages.success(request, 'successful')                     
    else:
        editblog = EditBlogForm(instance=editblog)
    return render(request, 'dashboard/editpost.html',{'edit':editblog})

def view_post(request,pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'dashboard/viewpost.html', {'post':post}) 
    return redirect('dashboard:viewblog') 

def delete_post(request,pk):
    record= get_object_or_404(Blog, pk=pk)
    record.delete()
    return redirect('dashboard:viewblog')

def logout_request(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.') 
    return redirect('index')   


