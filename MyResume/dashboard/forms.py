from django import forms
from dashboard.models import Project, Interest, Course

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'about', 'description', 'detail', 'result', 'image']
        

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['title', 'description', 'image']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'about', 'description', 'image']
