from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.forms import ModelForm

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    groups = models.ForeignKey(Group, null=True, related_name='projects')
    def __str__(self):
        return self.project_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    def __str__(self):
        return self.tag_name

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, max_length=200, on_delete=models.CASCADE, null=True, related_name='tasks')
    description = models.CharField(max_length=2000, null=True, blank=True)
    user = models.ForeignKey(User, null=True, related_name='tasks')
    tag = models.ManyToManyField(Tag, related_name='tasks')
    priority = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.task_name



class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'groups']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_name','project','description','priority']