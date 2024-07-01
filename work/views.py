from django.shortcuts import render
from django.views.generic import View
from work.forms import Register,LoginForm
from work.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

# C R U D

class Registration(View):
    def get(self,request,**kwargs):
        form=Register()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,**kwargs):
        form=Register(request.POST)
        if form.is_valid():
            
            User.objects.create_user(**form.cleaned_data)
            # create_user is used to encrypt the password.ie, only the user knows the password.only then the login will supports
            form=Register()
            return render(request,"register.html",{"form":form})
        
class Signin(View):
    
    def get(self,request,**kwargs):
        form=LoginForm()
        
        return render(request,"login.html",{"form":form})
    
    def post(self,request,**kwargs):
        form=LoginForm(request.POST)
        
        if form.is_valid():    #username,pssword
            print(form.cleaned_data)
            
            u_name=form.cleaned_data.get("username")
            # getting username and password from cleaned_data   
            pwd=form.cleaned_data.get("password")
            
            user_obj=authenticate(username=u_name,password=pwd)
            # checking if the username and password are valid in the table auth_user
            
            if user_obj:
                print("valid credentials")
                # if true, passing the user_obj to the login function
                login(request,user_obj)
                return render(request,"index.html")
            
            else:
                form=LoginForm()
                return render(request,"login.html",{"form":form})
                
            