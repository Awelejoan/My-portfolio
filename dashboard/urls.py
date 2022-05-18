from django.urls import path
from dashboard import views
from dashboard.forms import *


app_name ='dashboard'

urlpatterns =[
    path('dashboard/', views.dash, name='dashboard'),
    path('login/', views.log, name='login'),
    path('addblog/', views.addblog, name='addblog'),
    path('viewblog/', views.viewblog, name='viewblog'),
    path('changepassword/', views.passwordview, name='changepassword'),
    path('profile/', views.profilepage, name='profile'),
    path('editprofile/', views.edit_profile, name='editprofile'),
    path('editpost/<int:pk>', views.edit_post, name='editpost'),
    path('viewpost/<int:pk>', views.view_post, name='viewpost'),
    path('delete/<int:pk>', views.delete_post, name='delete'),
    path('logout/', views.logout_request, name='logout')
    

]