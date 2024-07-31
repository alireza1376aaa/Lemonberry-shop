from django.urls import path, include
# from account_shop.views import Log_in, Log_out, Register, Edit_user, forget_pass, forget_pass_reset
from django.contrib.auth import views as auth_views
from .views import Register_User, Log_in, Log_out, Edit_user ,forget_pass,forget_pass_reset

app_name = "account_shop"

urlpatterns = [
    path('register', Register_User, name='register'),
    path('login', Log_in, name='login'),
    path('logout', Log_out, name='loginout'),
    path('edit', Edit_user, name='Edit'),
    path('forget_pass', forget_pass, name='password_reset'),
    path('forget_pass/<code>', forget_pass_reset, name='forget_reet'),

]
