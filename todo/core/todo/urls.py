from django.urls import path
from .views import (HomepageView, TaskView, TaskUpdate, 
                                  TaskDelete, TaskCreate)

urlpatterns= [
    path('',HomepageView.as_view(), name = 'home'),
    path('task/<slug:slug>',TaskView.as_view(), name = 'task'),
    path('new/',TaskCreate.as_view(), name= 'addtask'),
    path('update/<slug:slug>',TaskUpdate.as_view(), name= 'update'),
    path('delete/<slug:slug>',TaskDelete.as_view(), name= 'delete'),
]