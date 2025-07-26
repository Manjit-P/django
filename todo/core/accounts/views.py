from django.urls import reverse_lazy
from .forms import CustomUserCreation
from django.views.generic import CreateView

class SignupView(CreateView):
    form_class = CustomUserCreation
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'