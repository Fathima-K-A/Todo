from django import forms
from work.models import User,Taskmodel

class Register(forms.ModelForm):
    
    class Meta:
        
        model=User
        fields=['username',"first_name","last_name","email","password"]
        
        
class TaskForm(forms.ModelForm):
    
    class Meta:
       
        model=Taskmodel
        fields=["task_name","task_description"]
        

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()