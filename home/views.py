from django.shortcuts import render
from .models import Project, Resume

from django.http import HttpResponse
from django.contrib.auth.models import User

# HOME PAGE
def index(request):
    skills = [
        "Python", "Data Analytics", "Machine Learning", "Power BI", "SQL",
        "Streamlit", "Django", "FastAPI", "MySQL", "PostgreSQL", "Git", "REST APIs"
    ]
    return render(request, "index.html", {"skills": skills})

# PROJECTS PAGE
def projects(request):
    projects = Project.objects.all()

    for project in projects:
        if project.tech_stack:
            project.tech_list = [
                tech.strip() for tech in project.tech_stack.split(',')
            ]
        else:
            project.tech_list = []

    return render(request, "projects.html", {"projects": projects})

# RESUME PAGE
def resume(request):
    resume = Resume.objects.last()
    return render(request, "resume.html", {"resume": resume})


# CONTACT PAGE
def contact(request):
    return render(request, "contact.html")


def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "Password123")
        return HttpResponse("Admin created successfully!")
    return HttpResponse("Admin already exists!")
