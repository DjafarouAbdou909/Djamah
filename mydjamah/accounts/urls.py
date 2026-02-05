from django.urls import path
from . import views
from django.contrib.auth import views as view

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logOut, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    #renitialisation du mot de passe
    path('resset_password', view.PasswordResetView.as_view(template_name = "password_reset.html"), name="resset_password"),
    path('resset_password_send', view.PasswordChangeDoneView.as_view(template_name = "password_reset.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', view.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete', view.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name="password_reset_complete"),

]