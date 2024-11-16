from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from dashboard.models import Project, Course

def education_view(request: HttpRequest):
    return render(request, "resume/education.html")


def projects_view(request: HttpRequest):
    projects = Project.objects.all()
    
    return render(request, "resume/projects.html", {"projects": projects})

def project_detail_view(request: HttpRequest, project_id:int):
    project = Project.objects.get(pk=project_id)
    
    return render(request, "resume/project_detail.html", {"project": project})


def events_view(request: HttpRequest):
    events = Course.objects.all()
    
    return render(request, "resume/events.html", {"events": events})

def event_detail_view(request: HttpRequest, event_id:int):
    event = Course.objects.get(pk=event_id)
    
    return render(request, "resume/event_detail.html", {"event": event})