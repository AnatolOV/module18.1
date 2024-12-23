from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from task5.forms import UserRegister

# Псевдо-список пользователей
users = ["user1", "user2", "user3"]


def process_registration(request):
    # Пустой словарь для информации
    info = {}

    form = UserRegister(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')

            # Простая проверка на существующих пользователей
            if username in users:
                info['error'] = "Пользователь с таким именем уже существует."
            elif password != repeat_password:
                info['error'] = "Пароли не совпадают."
            else:
                users.append(username)
                info['success'] = "Вы успешно зарегистрированы!"
                return render(request, 'registration/registration_page.html', {'form': UserRegister(), 'info': info})

    return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info})


def sign_up_by_django(request):
    return process_registration(request)

def sign_up_by_html(request):
    return process_registration(request)