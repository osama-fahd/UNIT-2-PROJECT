from django.db import models

class Project(models.Model):
    class Category(models.TextChoices):
        AI = 'ai', 'AI'
        FullStack = 'full', 'FullStack'
        FrontEnd = 'front', 'FrontEnd'
        BackEnd = 'back', 'BackEnd'
        DataAnalysis = 'analysis', 'DataAnalysis'

    category = models.CharField(choices=Category.choices, max_length=30, default=Category.FullStack)    
    title = models.CharField(max_length=1024)
    about = models.TextField()
    image = models.ImageField(upload_to="images/")
    
    description = models.TextField()
    section1 = models.TextField(default='Default text for section 1')
    section2 = models.TextField(default='Default text for section 2')
    section3 = models.TextField(default='Default text for section 3')
    section4 = models.TextField(default='Default text for section 4')
    skills = models.TextField(default='Default skills')

    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    

class Course(models.Model):
    class Category(models.TextChoices):
        AI = 'ai', 'AI'
        CLOUD = 'cloud', 'Cloud'
        FullStack = 'full', 'FullStack'
        FrontEnd = 'front', 'FrontEnd'
        BackEnd = 'back', 'BackEnd'
        DataAnalysis = 'analysis', 'DataAnalysis'

    category = models.CharField(choices=Category.choices, max_length=30, default=Category.FullStack)
    title = models.CharField(max_length=1024)
    about = models.TextField()
    image = models.ImageField(upload_to="images/")
    
    description = models.TextField()
    section1 = models.TextField(default='Default text for section 1')
    section2 = models.TextField(default='Default text for section 2')
    section3 = models.TextField(default='Default text for section 3')
    section4 = models.TextField(default='Default text for section 4')
    skills = models.TextField(default='Default skills')

    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class Interest(models.Model):
    
    title = models.CharField(max_length=1024)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
