from django.shortcuts import render, redirect
from todo.models import Project, Task, Tag, ProjectForm, TaskForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.utils import timezone


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


def process_proj_task_forms(request):
    if 'newproject' in request.POST:
        form = ProjectForm(request.POST)
        form.save()
        lastproject = Project.objects.get(project_name=request.POST['project_name'])
    elif 'newtask' in request.POST:
        form = TaskForm(request.POST)
        form.save()
        lastproject = request.POST['project']
    return lastproject

# Create your views here.

@login_required
def mainview(request):

    lastproject = None
    if request.method == 'POST':
        lastproject = process_proj_task_forms(request)


    project_list = [ p for p in Project.objects.all() if p.groups in request.user.groups.all() and p.isactive == True]
    print(lastproject)

    form = ProjectForm(initial={'groups':Group.objects.get(name=request.user.username)}   )
    form.fields['groups'].queryset = request.user.groups.all()
    
    context = {'project_list':project_list,
               'projectform':form,
               'taskform':TaskForm(initial={'project':lastproject})
               }

    return render(request, 'todo/mainview.html',context)

@login_required
def projectview(request,pk):

    if request.method == 'POST':
        process_proj_task_forms(request)

    proj = Project.objects.get(id=pk)
    context = {'project':proj, 'taskform':TaskForm(initial={'project':proj}) }
    return render(request,'todo/project.html',context)

@login_required
def completetask(request,pk):
    task = Task.objects.get(id=pk)
    pid = task.project.id

    #Flip whether task is or is not complete
    task.iscomplete = not task.iscomplete
    task.date_complete = timezone.now()
    task.save()
    return redirect('/todo/project/{}'.format(pid))


@login_required
def removeproj(request,pk):
    proj = Project.objects.get(id=pk)

    proj.isactive = not proj.isactive
    proj.save()
    return redirect('/todo/')
