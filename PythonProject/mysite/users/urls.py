from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView
from django.urls import path
from django.conf.urls.static import static

from mysite import settings
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUserView.as_view(),
         name='login'),
    path('logout/', views.logout_view,
         name='logout'),
    path('register/', views.RegisterUserView.as_view(),
         name='register'),
    path('user_profile/', views.UserDetailView.as_view(),
         name='user_profile'),
    path('user_profile/update/', views.UserUpdateView.as_view(),
         name='user_profile_update'),
    path('user_profile/change_password/', views.UserChangePasswordView.as_view(),
         name='change_password'),
    path('user_profile/change_password/done', PasswordChangeDoneView.as_view(
        template_name="users/password_change_done.html"),
         name='password_change_done'),
    path('password_reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(
        template_name="users/password_reset_done.html"),
         name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetDoneView.as_view(
        template_name="users/password_reset_complete.html"),
         name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

