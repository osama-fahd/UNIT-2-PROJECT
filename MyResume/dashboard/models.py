from django.db import models

class Project(models.Model):
    
    title = models.CharField(max_length=1024)
    about = models.TextField()
    description = models.TextField()
    detail = models.TextField()
    result = models.TextField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now=True)
    

class Interest(models.Model):
    
    title = models.CharField(max_length=1024)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now=True)
    

class Course(models.Model):
    
    title = models.CharField(max_length=1024)
    about = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now=True)