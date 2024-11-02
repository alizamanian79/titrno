from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new



from django.conf import settings

from django.views.static import serve

urlpatterns = [  
    path('admin/', admin.site.urls),  # Admin site  
    path('accounts/', include('accounts.urls')),  # Include URLs from accounts app  
    path('', include('website.urls')),  # Include URLs from website app  

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]  

