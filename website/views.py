from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from .models import New
from django.db.models import Q

# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')






def newpage_view(request, slug=None):  
    searchNews = []  
    q = request.GET.get("q")  

    if q:  
        
        searchNews = New.objects.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(slug__icontains=q))  

   
    new = get_object_or_404(New, active=True, slug=slug)  
    similarNews = New.objects.filter(active=True, categories__in=new.categories.all()).exclude(id=new.id).distinct()  

    # Render the response with the context  
    return render(request, 'website/new-page.html', {  
        "new": new,  
        "similarNews": similarNews,  
        "searchNews": searchNews  
    })  