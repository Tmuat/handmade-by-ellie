from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
)

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    This code is taken from the following tutorial:
    https://testdriven.io/blog/django-custom-user-model/
    """

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    """
    This code is taken from the following tutorial:
    https://testdriven.io/blog/django-custom-user-model/
    """

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
