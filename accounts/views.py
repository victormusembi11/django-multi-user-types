"""Account views."""
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView

from .decorators import student_required, teacher_required
from .forms import StudentSignupForm, TeacherSignupForm
from .models import User


class StudentSignupView(CreateView):
    """Student signup form."""

    model = User
    form_class = StudentSignupForm
    template_name = 'signup/student.html'

    def get_context_data(self, **kwargs):
        """Set user type to student in context dict."""
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        """Save, login user & redirect to home if form is valid."""
        user = form.save()
        login(self.request, user)
        return redirect('student_dashboard')


@method_decorator([login_required, student_required], name='dispatch')
class StudentDashboardView(TemplateView):
    """Student dashboard."""

    template_name = 'student/dashboard.html'


class TeacherSignupView(CreateView):
    """Teacher signup form view."""

    model = User
    form_class = TeacherSignupForm
    template_name = 'signup/teacher.html'

    def get_context_data(self, **kwargs):
        """Set user type to teacher in context dict."""
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        """Save, login user & redirect to home if form is valud."""
        user = form.save()
        login(self.request, user)
        return redirect('home')


@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherDashboardView(TemplateView):
    """Teacher Dashboard."""

    template_name = 'teacher/dashboard.html'
