from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import Buyer, Game


def main_page(request):
    return render(request, 'third_task/main_page.html')


def store_page(request):
    games = Game.objects.all()  # Получаем все записи из таблицы Game
    return render(request, 'third_task/store_page.html', {'games': games})


def cart_page(request):
    return render(request, 'third_task/card_page.html')


def registration_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            age = form.cleaned_data.get('age')
            balance = 0  # Предположим, что баланс у нового пользователя равен 0

            # Проверяем, существует ли пользователь с таким именем
            if not Buyer.objects.filter(name=username).exists():
                # Создаем нового пользователя
                Buyer.objects.create(name=username, age=age, balance=balance)
                return redirect('store_page')
            else:
                # Если пользователь уже существует, добавляем сообщение об ошибке
                form.add_error('username', 'Пользователь с таким именем уже существует')
    else:
        form = UserRegisterForm()

    return render(request, 'third_task/registration_page.html', {'form': form})
