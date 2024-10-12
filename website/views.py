from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from .models import New
from .forms import ContactForm
from django.db.models import Q
from django.http import Http404


# Create your views here.
def index_view(request):
    if request.method=="POST":
        form = ContactForm(request.POST)  
        if form.is_valid():  
            form.save()  
            messages.success(request, "Your message has been sent successfully.")  
            return redirect("/")  
        else:  
            messages.error(request, "There was an error sending your message.")

    form = ContactForm()
    return render(request, 'website/index.html',{
        "form": form,
    })


def newpage_view(request, slug=None):  


    searchNews = []  
    q = request.GET.get("q")  

    if q:  
        searchNews = New.objects.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(slug__icontains=q))  

    if request.method=="POST":
        form = ContactForm(request.POST)  
        if form.is_valid():  
            form.save()  
            messages.success(request, "Your message has been sent successfully.")  
            return redirect("/")  
        else:  
            messages.error(request, "There was an error sending your message.")



    form = ContactForm()
    new = get_object_or_404(New, active=True, slug=slug)  
    similarNews = New.objects.filter(active=True, categories__in=new.categories.all()).exclude(id=new.id).distinct()  

    # Render the response with the context  
    return render(request, 'website/new-page.html', {  
        "new": new,  
        "similarNews": similarNews,  
        "searchNews": searchNews ,
        "form": form 
    })  