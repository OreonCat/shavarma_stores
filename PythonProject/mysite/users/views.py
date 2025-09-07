
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, get_user_model
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from users.forms import LoginForm, RegisterForm, UserUpdateForm, UserChangePasswordForm


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Авторизация'
    }

class RegisterUserView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    extra_context = {
        'title': 'Регистрация'
    }

class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'users/detail.html'
    context_object_name = 'user_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['user_profile'].username
        return context

    def get_object(self):
        return self.request.user

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    extra_context = {
        'title': 'Редактировать профиль'
    }
    def get_success_url(self):
        return reverse_lazy('users:user_profile')

    def get_object(self):
        return self.request.user

class UserChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserChangePasswordForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change.html'


class UserPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



