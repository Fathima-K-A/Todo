from django.db import models
from django.contrib.auth.models import User


# user>>AbstractBaseUser>>BaseUser

class Taskmodel(models.Model):
    task_name=models.CharField( max_length=50)
    
    task_description=models.TextField()
    
    created_date=models.DateField(auto_now=True)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    completed=models.BooleanField(default=False)
    


