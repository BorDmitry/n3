from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name="profiles"),  #  главная страницая всего проекта ¨devsearch¨
    path('profile/<str:pk>/', views.user_profile, name="user_profile"),  # путь стр профиля разр-ка

    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),

]
