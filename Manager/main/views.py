from django.shortcuts import render,redirect

from .forms import TaskForm
from .models import Task
from django.views.generic import DetailView, UpdateView, DeleteView


def home(request):
    tasks = Task.objects.order_by('pk')
    return render(request, 'main/index.html',{'tasks':tasks})


def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/')
    form = TaskForm()
    context = {
        'form': form,

    }
    return render(request, 'main/create.html',context)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'main/details-view.html'
    context_object_name = 'post'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'main/create.html'

    form_class = TaskForm


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'main/task-delete.html'

