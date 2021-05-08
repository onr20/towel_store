from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'accounts'
urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("password_change/", views.MyPasswordChangeView.as_view(), name='password_change'),
    path("sign_up/", views.MySignUpView.as_view(), name='sign_up'),
]




