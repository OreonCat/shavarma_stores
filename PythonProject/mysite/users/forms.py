from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите')
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'photo', 'date_of_birth']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }
        widgets = {
            'email': forms.EmailInput,
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}, ),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с данным мылом существует")
        else:
            return email

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(disabled=True, max_length=100, label="Логин")
    email = forms.EmailField(disabled=True, max_length=100, label="E-mail")
    photo = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'photo', 'date_of_birth']
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия"
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}, ),
        }

class UserChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Повторите", widget=forms.PasswordInput)