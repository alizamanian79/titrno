from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from .models import New
# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')






def newpage_view(request, **kwargs):
    get_slug = kwargs["slug"]
    
    # Retrieve the news item by slug
    new = get_object_or_404(New, active=True, slug=get_slug)
    
    # Retrieve similar news items based on shared categories
    similarNews = New.objects.filter(active=True, categories__in=new.categories.all()).exclude(id=new.id).distinct()
  
    return render(request, 'website/new-page.html', {"new": new, "similarNews": similarNews})