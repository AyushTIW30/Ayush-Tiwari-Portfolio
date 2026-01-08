from django.db import models
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    image = CloudinaryField('image', blank=True, null=True)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.title



class Resume(models.Model):
    file = models.FileField(upload_to='resume/')
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Resume"
