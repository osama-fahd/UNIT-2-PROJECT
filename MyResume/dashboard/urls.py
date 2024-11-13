from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.dashboard_view, name="dashboard_view"),
    path("contact/messages/", views.contact_messages_view, name="contact_messages_view"),
]