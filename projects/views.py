from django.shortcuts import render
from projects.models import Project


# Create your views here.
# logic goes here (BACKEND)

def all_projects(request):
    """returns an object with all projects from the database"""

    # query the db to return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects': projects})


def project_detail(request, pk):
    """returns a single project as an object"""
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html', {'project': project})
