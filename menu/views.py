from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'menu/demo.html', {'page_title': 'Главная'})


def about(request):
    return render(request, 'menu/demo.html', {'page_title': 'О нас'})


def services(request):
    return render(request, 'menu/demo.html', {'page_title': 'Услуги'})


def contact(request):
    return render(request, 'menu/demo.html', {'page_title': 'Контакты'})


def portfolio(request):
    return render(request, 'menu/demo.html', {'page_title': 'Портфолио'})


def blog(request):
    return render(request, 'menu/demo.html', {'page_title': 'Блог'})
