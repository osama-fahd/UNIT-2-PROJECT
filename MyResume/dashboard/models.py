from django.db import models

class Project(models.Model):
    class Category(models.TextChoices):
        AI = 'ai', 'AI'
        FullStack = 'full', 'FullStack'
        FrontEnd = 'front', 'FrontEnd'
        BackEnd = 'back', 'BackEnd'
        DataAnalysis = 'analysis', 'DataAnalysis'

    category = models.CharField(choices=Category.choices, max_length=30)    
    title = models.CharField(max_length=1024)
    about = models.TextField()
    image = models.ImageField(upload_to="images/")
    
    description = models.TextField()
    section1 = models.TextField()
    section2 = models.TextField()
    section3 = models.TextField()
    section4 = models.TextField()
    skills = models.CharField(max_length=2048)

    created_at = models.DateTimeField(auto_now=True)
    

class Course(models.Model):
    class Category(models.TextChoices):
        AI = 'ai', 'AI'
        CLOUD = 'cloud', 'Cloud'
        FullStack = 'full', 'FullStack'
        FrontEnd = 'front', 'FrontEnd'
        BackEnd = 'back', 'BackEnd'
        DataAnalysis = 'analysis', 'DataAnalysis'

    category = models.CharField(choices=Category.choices, max_length=30)
    title = models.CharField(max_length=1024)
    about = models.TextField()
    image = models.ImageField(upload_to="images/")
    
    description = models.TextField()
    section1 = models.TextField()
    section2 = models.TextField()
    section3 = models.TextField()
    section4 = models.TextField()
    skills = models.CharField(max_length=2048)

    created_at = models.DateTimeField(auto_now=True)
    
    
class Interest(models.Model):
    
    title = models.CharField(max_length=1024)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now=True)
    
