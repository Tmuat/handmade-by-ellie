from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse

from users.models import UserProfile


def profile(request):
    """
    Display the user's profile.
    """

    template = "users/profile.html"
    context = {}

    return render(request, template, context)
