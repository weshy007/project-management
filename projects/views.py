from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, TaskForm
from .models import Project, Task
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
@login_required
def project_list(request):
    projects = Project.objects.all()
    
    return render(request, 'projects.html', {'projects': projects})


@login_required
def projectDetail(request,pk):
   project = get_object_or_404(Project, id=pk)
   project_tasks = project.task_set.all()
   
   context = {
        'project':project,
        'project_tasks':project_tasks}
   
   return render(request, 'project-detail.html', context)


@login_required
def task_list(request):
    user_tasks = Task.objects.filter(assignee=request.user)
    tasks = Task.objects.filter(assignee=None)

    context = {
        'tasks':tasks,
        'user_tasks':user_tasks
    }

    return render(request, 'tasks.html', context)


@login_required
def task_detail(request, pk):
    task = Task.objects.get(id=pk)

    return render(request, 'task-detail.html', {'task': task})


@login_required
def task_create(request):
    form = TaskForm
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    
    return render(request, 'task-create.html', {'form': form})


@login_required
def join_task(request, pk):
    task = Task.objects.get(id=pk)
    task.assignee=request.user
    task.save()
    return redirect('tasks')

class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    fields = ["name","description"]
    template_name = 'project_create_form.html'
    success_url = reverse_lazy('projects')


class ProjectUpdateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project_update_form.hmtl'
    fields = ['name', 'description']
    success_url = reverse_lazy('projects')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('projects')


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'task_update_form.html'
    fields = ['title', 'description', 'project', 'assignee', 'due_date', 'status']
    success_url = reverse_lazy('tasks')


class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'projects/task_confirm_delete.html'
    success_url = reverse_lazy('tasks')

