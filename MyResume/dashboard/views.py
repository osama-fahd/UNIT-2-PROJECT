from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def dashboard_view(request: HttpRequest):
    
    return render(request, "dashboard/dashboard.html")

def contact_messages_view(request: HttpRequest):
    
    return render(request, "dashboard/contact_messages.html")