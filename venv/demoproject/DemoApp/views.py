from django.shortcuts import render , redirect
from .form import ProjectForm
from .models import Project
# Create your views here.

projectlist=[
    {'id':'1',
    'title':'Ecommerce website',
    'description':'Fully functional ecommerce website'
    },
    {'id':'2',
    'title':'Portofolio Website',
    'description':'This was a project where I bulitout my portolio'
    },
    {'id':'3',
    'title':'social Network',
    'description':'Awesome open source project I am working'
    },
    {'id':'4',
    'title':' Social Media Platform',
    'description':'This the platform were community interact'
    },
]

def dashboard(request):
    object= Project.objects.all()
    msg= "django is amazing frame python-web-work"

    number= 20
    context={'text':msg, 'number': number, 'projects':projectlist, 'object':object}

    return render(request, 'DemoApp/dashboard.html',context)

def index(request, pk):
    projectobj = None
    for project in projectlist:
        if project['id']==pk:
            projectobj=project
    
    project= Project.objects.get(id=pk)

    context={'project': projectobj, 'project':project}

    return render(request, 'DemoApp/index.html', context)

def createproject(request):
    formobj= ProjectForm(request.POST)
    if formobj.is_valid():
        formobj.save()
        return redirect('dashboard')

    context= {'form':formobj}
    return render (request, 'DemoApp/project_form.html', context)

def updateProject(request,pk):
    project= Project.objects.get(id=pk)
    form= ProjectForm(instance=project)
    if request.method =="POST":
        form= ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context= {'form':form}
    return render(request, 'DemoApp/project_form.html', context)

def deleteProject(request, pk):
    project= Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('dashboard')
    context={'project':project}
    return render(request, 'DemoApp/delete_project.html', context)




