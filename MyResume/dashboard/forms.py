from django import forms
from dashboard.models import Project, Interest, Course

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'about', 'description', 'image', 'category', 'section1', 'section2', 'section3', 'section4', 'skills']
        

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'about', 'description', 'image', 'category', 'section1', 'section2', 'section3', 'section4', 'skills']
        

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['title', 'description', 'image']

