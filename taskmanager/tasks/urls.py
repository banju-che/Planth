from django.urls import path
from . import views

urlpatterns = [
    # Project routes
    path('projects/', views.project_list_create, name='project-list-create'),
    path('projects/<int:pk>/', views.project_detail, name='project-detail'),

    # Task routes
    path('tasks/', views.task_list_create, name='task-list-create'),
    path('tasks/<int:pk>/', views.task_detail, name='task-detail'),
    path('tasks/<int:pk>/assign/', views.assign_task, name='task-assign'),

    # Comment routes
    path('tasks/<int:task_id>/comments/', views.add_comment, name='add-comment'),
    path('comments/<int:pk>/delete/', views.delete_comment, name='delete-comment'),

    path('auth/register/', views.register_user, name='register'),

    path('api/user/profile/', views.get_user_profile),

]
