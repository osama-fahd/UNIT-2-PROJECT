from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.dashboard_view, name="dashboard_view"),
    
    path("contact/messages/", views.contact_messages_view, name="contact_messages_view"),
    path("delete/message/<message_id>/", views.delete_contact_message_view , name="delete_contact_message_view"),
    
    path("project/", views.project_view , name="project_view"),
    path("interest/", views.interest_view , name="interest_view"),
    path("course/", views.course_view , name="course_view"),
    
    path("add/project/", views.add_project_view , name="add_project_view"),
    path("add/interest/", views.add_interest_view , name="add_interest_view"),
    path("add/course/", views.add_course_view , name="add_course_view"),
    
    path("update/project/<project_id>/", views.update_project_view , name="update_project_view"),
    path("update/interest/<interest_id>/", views.update_interest_view , name="update_interest_view"),
    path("update/course/<course_id>/", views.update_course_view , name="update_course_view"),
    
    path("delete/project/<project_id>/", views.delete_project_view , name="delete_project_view"),
    path("delete/interest/<interest_id>/", views.delete_interest_view , name="delete_interest_view"),
    path("delete/course/<course_id>/", views.delete_course_view , name="delete_course_view"),
    
    path("search/", views.search_view, name="search_view")
]