from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def projects(request):        # обработчик стр-цы со всеми проектами
    pr = Project.objects.all()
    context = {'projects': pr}
    return render(request, "projects/projects.html", context)


def project(request, pk):    # pk - для просмотра индивидуального проекта
    project_obj = Project.objects.get(id=pk)  # получаем данные те, у кот соотв-й id попадёт в адресн. строку
    return render(request, 'projects/single-project.html', {'project': project_obj})


def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/form-template.html', context)
