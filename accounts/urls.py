from django.urls import path
from . import views


app_name="accounts"
urlpatterns = [
    path('login/', views.signIn, name='login'),
    path('signup/', views.signupView, name='signup'),
    path('logout/', views.logoutView, name='logout'),
]
