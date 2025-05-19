from django.shortcuts import render
from .models import User


def home(request):
    data = User.objects.all()
    context = {
        'data': data
    }
    return render(request, "home.html", context)
