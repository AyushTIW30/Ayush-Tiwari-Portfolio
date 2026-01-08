from django.contrib import admin
from django.http import HttpResponse
from .models import Project, Resume
from django.contrib.auth.models import User



admin.site.register(Project)
admin.site.register(Resume)
