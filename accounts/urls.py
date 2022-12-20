"""Account URL's."""
from django.urls import include, path

from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup/student/", views.StudentSignupView.as_view(), name="student_signup"),
    path(
        "student/dashboard/",
        views.StudentDashboardView.as_view(),
        name="student_dashboard",
    ),
    path("signup/teacher/", views.TeacherSignupView.as_view(), name="teacher_signup"),
]
