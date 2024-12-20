from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Contact
from .forms import ContactForm

from dashboard.models import Interest, Project


def home_view(request: HttpRequest):
    interests = Interest.objects.all()
    projects = Project.objects.filter(category=Project.Category.AI)
    
    return render(request, "main/home.html", {"interests": interests, "projects": projects})

def contact_view(request: HttpRequest):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('main:home_view')
        else:
            return render(request, "main/contact.html")
    
    return render(request, "main/contact.html")

def contact_messages_view(request: HttpRequest):
    
    return render(request, "main/contact_messages.html")