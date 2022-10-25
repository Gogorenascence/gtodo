from django.shortcuts import render
from tasks.models import Task
from django.contrib.auth.decorators import login_required


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "tasks/mine.html", context)
