"""Account URL's."""
from django.urls import include, path

from . import views

urlpatterns = [
    path("signup/student/", views.StudentSignupView.as_view(), name="student_signup"),
    path(
        "student/dashboard/",
        views.StudentDashboardView.as_view(),
        name="student_dashboard",
    ),
    path("teacher/dashboard/", views.TeacherDashboardView.as_view(), name="teacher_dashboard"),
    path("signup/teacher/", views.TeacherSignupView.as_view(), name="teacher_signup"),
    path("login/student/", views.StudentLoginView.as_view(), name="student_login"),
    path("login/teacher/", views.TeacherLoginView.as_view(), name="teacher_login"),
    path("", include("django.contrib.auth.urls")),
]
