from django.urls import path
from . import views

app_name="website"
urlpatterns = [
    path("",views.index_view,name="index"),
    path('category/search/<path:cat>/',views.index_view, name='search_category'),
    path('tag/search/<path:tag>/',views.index_view, name='search_tag'),
    path('journalist/search/<path:journalist>/',views.index_view, name='search_journalist'),


    path('new/<str:slug>/',views.newpage_view, name='newpage'),

    
    # Crud News Api with CBV
    path('api/new/',views.NewsListView.as_view(),name="news-list"),
    path('api/new/detail/<int:pk>/',views.NewDetailView.as_view(),name="new-detail"),
    path('api/new/delete/<int:pk>/',views.NewDeleteView.as_view(),name="new-delete"),
    path('api/new/update/<int:pk>/',views.NewUpdateView.as_view(),name="new-update"),
    path('api/new/create/',views.NewCreateView.as_view(),name="new-create"),
]
