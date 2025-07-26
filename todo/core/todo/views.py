from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task


class HomepageView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "home.html"


class TaskView(DetailView):
    model = Task
    template_name = "task.html"
    today = timezone.now()
    slug_field = "slug"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = [
        "name",
        "due",
        "category",
        "description",
    ]
    template_name = "addtask.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "update.html"
    slug_field = "slug"
    fields = [
        "name",
        "due",
        "category",
        "description",
    ]


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "delete.html"
    success_url = reverse_lazy("home")
    slug_field = "slug"
