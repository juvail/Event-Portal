from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.accounts, name="accounts"),
    path("login/" , views.login_view, name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("password-reset/",auth_views.PasswordResetView.as_view(template_name='password_reset.html') ,name="password_reset"),
    path("password-reset/done/",auth_views.PasswordResetDoneView.as_view(template_name='password_reset_send.html') , name="password_reset_done"),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name="password_reset_confirm"),
    path("reset/done/",auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_complete")
    ]