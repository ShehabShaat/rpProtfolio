from django.shortcuts import render
from projects.models import Project
# view is python function it perform when the the function reseive request

def project_index(request): 
    projects = Project.objects.all()
    context = {
    'projects': projects
    }
    return render(request, 'project_index.html', context)        

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)  