from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        module = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )