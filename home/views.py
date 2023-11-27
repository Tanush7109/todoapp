from django.shortcuts import render, redirect
from home.models import Task
# Create your views here.
def home(request):
    if request.method == "POST":
        title = request.POST['task']
        desc = request.POST['desc']
        ins = Task(task=title, task_desc=desc)
        ins.save()
        return redirect('/tasks/')

    return render(request, "base.html")

def tasks(request):
    status = ""
    allTasks = Task.objects.all()
    object_count = Task.objects.count()
    
    
    if object_count != 0:
        status = ""
    else:
        status = "No todos!"
        
        
    context = {
        'tasks': allTasks,
        'task_status': status
    }

    return render(request, "tasks.html", context)



def delete(request, id):
    specific_todo = Task.objects.get(id=id)
    specific_todo.delete()
    return redirect('/tasks')