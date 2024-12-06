from django.contrib import admin
from .models import Project, Interest, Course
from main.models import Contact


admin.site.register(Project)
admin.site.register(Interest)
admin.site.register(Course)
admin.site.register(Contact)
 
