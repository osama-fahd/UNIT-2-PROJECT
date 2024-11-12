from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def education_view(request: HttpRequest):
    return render(request, "resume/education.html")

def projects_view(request: HttpRequest):
    return render(request, "resume/projects.html")