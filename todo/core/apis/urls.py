from django.urls import path
from .views import TaskApiListView, TaskApiDetailView

urlpatterns = [
    path("<slug:slug>/", TaskApiDetailView.as_view(), name= 'task_detail'),
    path("", TaskApiListView.as_view(), name= 'task_list'),
]