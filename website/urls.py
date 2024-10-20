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
    path('manage/new/list/',views.NewsListView.as_view(),name="news-list"),
    path('manage/new/detail/<int:pk>/',views.NewDetailView.as_view(),name="new-detail"),
    path('manage/new/delete/<int:pk>/',views.NewDeleteView.as_view(),name="new-delete"),
    path('manage/new/update/<int:pk>/',views.NewUpdateView.as_view(),name="new-update"),
    path('manage/new/create/',views.NewCreateView.as_view(),name="new-create"),
]
