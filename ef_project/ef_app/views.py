from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Public, Private
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def home_page(request):
    categories = Category.objects.all()
    eventspb = Public.objects.all()

    context = {
        'categories': categories,
        'eventspb': eventspb
    }
    return render(request, "./home.html", context)

def home2_page(request):
    categories = Category.objects.all()
    eventspv = Private.objects.all()

    context = {
        'categories': categories,
        'eventspv': eventspv
    }
    return render(request, "./home2.html", context)

def about_page(request):
    return render(request, "./about.html")

def description_page(request, pk):
    eventpb = get_object_or_404(Public, pk=pk)
    eventspb = Public.objects.all()  # Получаем все мероприятия

    context = {
        'eventpb': eventpb,
        'eventspb': eventspb  # Передаём их в шаблон
    }
    return render(request, "./description.html", context)


def privatedesc_page(request, pk):
    eventpv = get_object_or_404(Private, pk=pk)
    eventspv = Public.objects.all()  # Получаем все мероприятия

    context = {
        'eventpv': eventpv,
        'eventspv': eventspv  # Передаём их в шаблон
    }
    return render(request, "./privatedesc.html", context)

def create_page(request):
    return render(request, "./create.html")

def settings_page(request):
    return render(request, "./settings.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("user_login")  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home_page")  # Redirect to the home page after successful login
            else:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Invalid credentials")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})