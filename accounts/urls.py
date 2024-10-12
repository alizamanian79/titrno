from django.urls import path
from .views import SignInView, LogoutView, SignUpView


app_name="accounts"
urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
