from django.urls import path
from . import views

urlpatterns = [
    path('', views.threads_list, name = "threads_list"),
    path('create/', views.threads_create, name = "threads_create"),
    path('<int:thread_id>/edit/', views.threads_edit, name = "threads_edit"),
    path('<int:thread_id>/delete/', views.threads_delete, name = "threads_delete"),
    path('register/', views.register, name = "register"),
    path('search/', views.search_thread, name='search_thread'),
]
