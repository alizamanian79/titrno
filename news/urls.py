from django.urls import path
from .views import index_view,newpage_view

app_name="news"
urlpatterns = [
    path("",index_view,name="index"),
    path("new/<str:slug>/",newpage_view,name="new-page"),
]
