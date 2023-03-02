from django.shortcuts import render, redirect
from . models import Profile
from django.contrib.auth import logout


def login_user(request):
    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def profiles(request):           # гл. стр. всех профилей
    prof = Profile.objects.all()
    context = {'profiles': prof}
    return render(request, 'users/index.html', context)


def user_profile(request, pk):       # стр профиля разработчика
    prof = Profile.objects.get(id=pk)

    top_skills = prof.skill_set.exclude(description__exact="") # исключить элементы, кот. содержат пуст. строку
    other_skills = prof.skill_set.filter(description="")  # элементы с пустым содержанием

    context = {
        'profile': prof,
        'top_skills': top_skills,
        'other_skills': other_skills
    }
    return render(request, 'users/profile.html', context)
