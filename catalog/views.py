from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home.html')

# def contacts(request):
#     return render(request, 'contacts.html')

def contacts(request):
    if request.method == 'POST':
        # Получаем данные из полей формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message_text = request.POST.get('message')

        # Проверяем, что поля не пустые (базовая валидация)
        if name and phone and message_text:
            # Здесь в будущем можно сохранять данные в БД, например:
            # Contact.objects.create(name=name, phone=phone, message=message_text)

            # Добавляем сообщение об успехе
            messages.success(request, f'Спасибо, {name}! Ваше сообщение успешно отправлено.')

            # Делаем редирект на эту же страницу, чтобы при обновлении (F5)
            # форма не отправлялась повторно
            return redirect('/contacts/')
        else:
            messages.error(request, 'Пожалуйста, заполните все поля.')

    # Если это GET-запрос, просто показываем страницу
    return render(request, 'contacts.html')