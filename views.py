from django.shortcuts import render
from todo.models import Project, Task, Tag, ProjectForm, TaskForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required


# Helper functions
def is_group_match(user1, user2):
    return any(x in user1.groups.all() for x in user2.groups.all())

def add_tags(tag_list, task):
    for tag in tag_list:
        try:
            tag_obj = Tag.objects.get(tag_name=tag)
        except:
            tag_obj = Tag(tag_name=tag)
            tag_obj.save()
        tag_obj.tasks.add(task)

def create_new_project(project_name,user):
    p = Project(project_name=project_name, group=user.username)
    p.save()
def create_new_task(project, task_name):
    t = Task(task_name='find new lesions', project=p, description='ID new lesions on SWI and see if they show up on hyperintense on FLAIR', user=user,priority=5)

# Create your views here.

@login_required
def mainview(request):

    lastproject = None

    if request.method == 'POST':
        if 'newproject' in request.POST:
            form = ProjectForm(request.POST)
            form.save()
        elif 'newtask' in request.POST:
            form = TaskForm(request.POST)
            form.save()
            lastproject = request.POST['project']
    
        

    project_list = [ p for p in Project.objects.all() if p.groups in request.user.groups.all() ]
    print(project_list)

    context = {'project_list':project_list, 
               'projectform':ProjectForm(initial={'groups':Group.objects.get(name=request.user.username)}), 
               'taskform':TaskForm(initial={'project':lastproject})
    }

    return render(request, 'todo/mainview.html',context)
