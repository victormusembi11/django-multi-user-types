"""Admin configuration."""
from django.contrib import admin

from .models import Student, User

admin.site.register(User)
admin.site.register(Student)
