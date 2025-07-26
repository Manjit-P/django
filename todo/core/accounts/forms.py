from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,
                                       PasswordResetForm, PasswordChangeForm,
                                       )
from .models import CustomUser

class CustomUserCreation(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'age',
        ]
class CustomUserChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'age',
        ]
