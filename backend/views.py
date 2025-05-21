from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserForm


def home(request):
    data = User.objects.all()

    context = {
        'data': data
    }

    return render(request, "home.html", context)


def add_data(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data has been added")
            return redirect("add_data")
        else:
            messages.error(request, "Invalid data")
    else:
        form = UserForm()

    return render(request, "add_data.html", {"form": form})

# def add_data(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         age = request.POST.get("age")
#         isMaried = request.POST.get("ismaried") == "on"
#
#         user_data = User(
#             name=name,
#             email=email,
#             age=age,
#             isMaried=isMaried,
#         )
#         try:
#             user_data.save()
#             messages.success(request, "Data Saved Successfully")
#         except Exception as e:
#             messages.error(request, f"Error Saving data to database: {e}")
#         return redirect('add_data')
#
#     return render(request, "add_data.html")
