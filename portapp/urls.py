from django.urls import path
from portapp import views
from django.contrib.auth import views as auth_views
from portapp.models import * 

app_name = 'portapp'

urlpatterns=[
    path('blog/', views.blog, name='blog'),
    path('blog-detail/<int:pk>', views.BlogDetail, name='blog_detail'),
    path('register/', views.regform, name='reg'),
    path('login/', views.login_user, name='login'),
    
    

]