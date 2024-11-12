from django.urls import path
from . import views

app_name = "resume"

urlpatterns = [
    path("education/", views.education_view, name="education_view"),
    path("projects/", views.projects_view, name="projects_view"),
]
