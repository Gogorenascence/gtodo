from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/home.html", context)


# @login_required
# def show_project(request):
#     project = Project.objects.get(id=id)
#     context = {
#         "project": pro
#     }
