from django.urls import path
from .views import register_view, login_view, logout_view, home_view, task_list, task_create, task_delete, task_update, about_view



urlpatterns = [
    path('', home_view, name="home"),
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('tasks/', task_list, name='task_list'),
    path('tasks/create/', task_create, name='task_create'),
    path('tasks/<int:pk>/update/', task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', task_delete, name='task_delete'),
    path('about/', about_view, name='about')
]