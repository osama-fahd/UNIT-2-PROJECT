from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Project, Interest, Course
from .forms import ProjectForm, InterestForm, CourseForm

from main.models import Contact


def dashboard_view(request: HttpRequest):
    projects = Project.objects.all()
    interests = Interest.objects.all()
    courses = Course.objects.all()
    messages = Contact.objects.all()
    
    return render(request, "dashboard/dashboard.html", {"projects": projects, "interests": interests, "courses": courses, "messages": messages})



def contact_messages_view(request: HttpRequest):
    messages = Contact.objects.all()
    
    return render(request, "dashboard/contact_messages.html", {"messages": messages})

def delete_contact_message_view(request:HttpRequest, message_id:int):
    message = Contact.objects.get(pk=message_id)
    message.delete()

    return redirect("dashboard:contact_messages_view")



def project_view(request: HttpRequest):
    projects = Project.objects.all()
    
    return render(request, "dashboard/project.html", {"projects": projects})

def interest_view(request: HttpRequest):
    interests = Interest.objects.all()
    
    return render(request, "dashboard/interest.html", {"interests": interests})
    
def course_view(request: HttpRequest):
    courses = Course.objects.all()
    
    return render(request, "dashboard/course.html", {"courses": courses})



def add_project_view(request: HttpRequest):
    project_form = ProjectForm()
    
    if request.method == "POST":
        project_form = ProjectForm(request.POST, request.FILES)
        if project_form.is_valid():
            project_form.save()
            return redirect('dashboard:project_view')
        
    return render(request, "dashboard/add_project.html", {"categories": Project.Category.choices})

def add_interest_view(request: HttpRequest):
    interest_form = InterestForm()
    
    if request.method == "POST":
        interest_form = InterestForm(request.POST, request.FILES)
        if interest_form.is_valid():
            interest_form.save()
            return redirect('dashboard:interest_view')
    
    return render(request, "dashboard/add_interest.html")

def add_course_view(request: HttpRequest):
    course_form = CourseForm()
    
    if request.method == "POST":
        course_form = CourseForm(request.POST, request.FILES)
        if course_form.is_valid():
            course_form.save()
            return redirect('dashboard:course_view')
        
    return render(request, "dashboard/add_course.html", {"categories": Course.Category.choices})



def update_project_view(request: HttpRequest, project_id:int):
    project = Project.objects.get(pk=project_id)
    
    if request.method == "POST":
        project.title = request.POST["title"]
        project.about = request.POST["about"]
        project.description = request.POST['description']
        project.section1 = request.POST['section1']
        project.section2 = request.POST['section2']
        project.section3 = request.POST['section3']
        project.section4 = request.POST['section4']
        project.skills = request.POST['skills']
        if "image" in request.FILES: project.image = request.FILES["image"]
        if "category" in request.POST: project.category = request.POST["category"]
        project.save()
        
        return redirect("dashboard:project_view")
    
    return render(request, "dashboard/update_project.html", {"project": project, "categories": Project.Category.choices})

def update_interest_view(request: HttpRequest, interest_id:int):
    interest = Interest.objects.get(pk=interest_id)
    
    if request.method == "POST":
        interest.title = request.POST["title"]
        interest.description = request.POST['description']
        if "image" in request.FILES: interest.image = request.FILES["image"]
        interest.save()
        
        return redirect("dashboard:interest_view")
    
    return render(request, "dashboard/update_interest.html", {"interest": interest})

def update_course_view(request: HttpRequest, course_id:int):
    course = Course.objects.get(pk=course_id)
    
    if request.method == "POST":
        course.title = request.POST["title"]
        course.about = request.POST["about"]
        course.description = request.POST['description']
        course.section1 = request.POST['section1']
        course.section2 = request.POST['section2']
        course.section3 = request.POST['section3']
        course.section4 = request.POST['section4']
        course.skills = request.POST['skills']
        if "image" in request.FILES: course.image = request.FILES["image"]
        if "category" in request.POST: course.category = request.POST["category"]
        course.save()
        
        return redirect("dashboard:course_view")
    
    return render(request, "dashboard/update_course.html", {"course": course, "categories": Course.Category.choices})



def delete_project_view(request:HttpRequest, project_id:int):
    project = Project.objects.get(pk=project_id)
    project.delete()

    return redirect("dashboard:project_view")

def delete_interest_view(request:HttpRequest, interest_id:int):
    interest = Interest.objects.get(pk=interest_id)
    interest.delete()

    return redirect("dashboard:interest_view")

def delete_course_view(request:HttpRequest, course_id:int):
    course = Course.objects.get(pk=course_id)
    course.delete()

    return redirect("dashboard:course_view")
