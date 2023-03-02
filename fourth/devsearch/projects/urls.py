from django.urls import path
from . import views


urlpatterns = [
    path("", views.projects, name="projects"),                # стр-ца, где выводятся все проекты
    path('project/<str:pk>/', views.project, name="project"), # стра-ца отдельного проекта

    path('create-project/', views.create_project, name="create-project"),
]

