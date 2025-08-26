from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),                     
    path("grading/", views.grading, name="grading"),
    path("prelim/", views.prelim_list, name="prelim_list"),
    path("students/new/", views.student_create, name="student_create"),
    path("prelim/new/", views.prelim_create, name="prelim_create"),
    path("midterm/new/", views.midterm_create, name="midterm_create"),
    path("finals/new/", views.final_create, name="final_create"),
]
