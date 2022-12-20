"""Account views."""
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

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
        return redirect('home')


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
