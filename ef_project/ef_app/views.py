from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Public, Private, PrivateCat
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import EventForm

# Create your views here.
def home_page(request):
    categoriespb = Category.objects.all()
    eventspb = Public.objects.all()

    context = {
        'categoriespb': categoriespb,
        'eventspb': eventspb
    }
    return render(request, "./home.html", context)

def home2_page(request):
    categoriespv = PrivateCat.objects.all()
    eventspv = Private.objects.all()

    context = {
        'categoriespv': categoriespv,
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
    eventspv = Private.objects.all()  # Получаем все мероприятия

    context = {
        'eventpv': eventpv,
        'eventspv': eventspv  # Передаём их в шаблон
    }
    return render(request, "./privatedesc.html", context)

def create_page(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Если ModelForm
            return redirect('home2_page')  # Замените на ваш URL
    else:
        form = EventForm()
        form.fields['category'].choices = [(c.id, c.name) for c in PrivateCat.objects.all()]  # Заполняем категории

    return render(request, 'create.html', {'form': form})

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

def page_by_category(request, slug):
    categorypb = get_object_or_404(Category, slug=slug)
    eventspb = Public.objects.filter(category=categorypb)  # Изменил categorypb на category

    context = {
        'categorypb': categorypb,
        'eventspb': eventspb
    }
    return render(request, "page_by_category.html", context)  # Убрал ./

def page_by_category_private(request, slug):
    categorypv = get_object_or_404(PrivateCat, slug=slug)
    eventspv = Private.objects.filter(category=categorypv)  # Изменил categorypv на category

    context = {
        'categorypv': categorypv,
        'eventspv': eventspv
    }
    return render(request, "page_by_category_private.html", context)  # Убрал ./


def search(request):
    query = request.GET.get('q', '').strip().lower()  # Убираем пробелы и приводим к нижнему регистру
    print(f"Поисковый запрос: {query}")  # Выводим в консоль

    eventspb = Public.objects.all()
    eventspv = Private.objects.all()

    if query:
        eventspb = eventspb.filter(title__icontains=query)
        eventspv = eventspv.filter(title__icontains=query)

    print(f"Найдено публичных: {eventspb.count()}, приватных: {eventspv.count()}")

    return render(request, 'search.html', {
        'eventspb': eventspb,
        'eventspv': eventspv,
        'query': query
    })

