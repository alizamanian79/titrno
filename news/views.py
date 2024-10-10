from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')

def newpage_view(request, **kwargs):  
    
    if kwargs.get("slug"):
        print(kwargs)
    
    context={"slug": kwargs.get("slug")}
    return render(request, 'website/new-page.html', context)  
