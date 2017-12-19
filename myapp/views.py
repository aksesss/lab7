from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic.edit import FormView

from .forms import *


def mainView(requests):
    title = "main"
    return render(requests, "main.html", locals())


def infoView(requests):
    title = "main"
    return render(requests, "info.html", locals())


class GoodsListView(ListView):
    model = Goods
    # model = model.objects.filter(good_id='1')
    # list_filter = ["good_id"]
    template_name = "goods.html"
    context_object_name = "obj_list"
    # queryset = "good_id=1"

    def get(self, request, *args, **kwargs):
         self.id = request.GET.get('id')
         return super(GoodsListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        if self.id:
            return Goods.objects.filter(good_id=self.id)
        else:
            return Goods.objects.all()




def goodsAddView(requests):
    main_text = "Добавить товар:"

    form = GoodsForm(requests.POST or None)
    log_in_is_success = False
    result = ''

    if requests.method == "POST" and form.is_valid():
        form.save()

        result = "Товар успешно добавлен!"

    return render(requests, "goods_add.html", locals())


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "log.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/main/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/main/")


def registrationmy(request):
    errors = {'username': '', 'password': '', 'password2': '', 'email': '', 'firstname': '', 'surname': ''}
    error_flag = False
    if request.method == 'POST':

        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'
            error_flag = True
        elif len(username) < 5:
            errors['username'] = 'Логин должен превышать 5 символов'
            error_flag = True
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Такой логин уже существует'
            error_flag = True

        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'
            error_flag = True
        elif len(password) < 8:
            errors['password'] = 'Длина пароля должна превышать 8 символов'

        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password2'] = 'Пароли должны совпадать'
            error_flag = True

        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите e-mail'

        firstname = request.POST.get('firstname')
        if not firstname:
            errors['firstname'] = 'Введите имя'
        surname = request.POST.get('surname')
        if not surname:
            errors['surname'] = 'Введите фамилию'

        if not error_flag:
            # ...
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname,
                                            last_name=surname)
            return HttpResponseRedirect('/login/')

    return render(request, 'reg_my.html', locals())
