from django.urls import path
from .views import index_view,newpage_view

app_name="website"
urlpatterns = [
    path("",index_view,name="index"),
    path('new/<slug:slug>/', newpage_view, name='newpage'),
   
]
