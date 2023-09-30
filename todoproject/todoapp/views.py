from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import TodoForms
from django.views.generic import ListView,DetailView,UpdateView,DeleteView

class Taklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'my_task'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


class Taskupdateview(UpdateView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cldetail',kwargs={'pk':self.object.id})


class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cltask')

# Create your views here.
def home(request):
    my_task = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        task = Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'my_task':my_task})

def details(request):

    return render(request,'details.html')

def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')


    return render(request,'delete.html')

def update(request,taskid):
    task= Task.objects.get(id=taskid)
    form = TodoForms(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'edit.html', {'task':task,'form':form})

