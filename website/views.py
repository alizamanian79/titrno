from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from .models import New,Category
from .forms import ContactForm,NewForm
from django.db.models import Q
from django.http import Http404
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
# Create your views here.
def index_view(request,**kwargs):
    news = New.objects.filter(active=True).order_by('-created_at')  
    categories=Category.objects.all()



    if kwargs.get("cat"):  
       news = news.filter(categories__title=kwargs["cat"])  
    
    if kwargs.get("tag"):  
       news = news.filter(tags__title=kwargs["tag"])  

    if kwargs.get("journalist"):  
       news = news.filter(journalist__username=kwargs["journalist"]) 


    if request.method=="POST":
       contactus(request)


    if q:=request.GET.get("q") : 
        news = New.objects.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(slug__icontains=q))  



    form = ContactForm()
    return render(request, 'website/index.html',{
        "form": form,
        "news": news,
        "categories":categories,
        "breakingnews":BreakingNewsLine(),
        "breakingSlider":getSlider("BREAKING"),
        "developingSlider":getSlider("DEVELOPING"),
        "exclusiveSlider":getSlider("EXCLUSIVE")
    })
def newpage_view(request, slug=None):  
    categories=Category.objects.all()

    searchNews = []  
    q = request.GET.get("q")  

    if q:  
        searchNews = New.objects.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(slug__icontains=q))  

    if request.method=="POST":
       contactus(request)

    form = ContactForm()
    new = get_object_or_404(New, active=True, slug=slug)  
    similarNews = New.objects.filter(active=True, categories__in=new.categories.all()).exclude(id=new.id).distinct()  
 
    return render(request, 'website/new-page.html', {  
        "new": new,  
        "categories":categories,
        "similarNews": similarNews,  
        "searchNews": searchNews ,
        "form": form 
    })  



class NewsListView(ListView):
    template_name="managenews/news-list.html"
    model=New
    context_object_name="news"

    def get_queryset(self):
        if q:=self.request.GET.get('q'):
            query_set=New.objects.filter(active=True,title__icontains=q)
            return query_set
        return super().get_queryset()



class NewDetailView(DetailView):
    template_name="managenews/new-detail.html"
    model=New
    context_object_name="new"


class NewDeleteView(DeleteView):
    template_name="managenews/new-delete.html"
    model=New
    context_object_name="new"
    success_url=reverse_lazy("website:news-list")

class NewUpdateView(UpdateView):
    template_name="managenews/new-form.html"
    model=New
    form_class=NewForm
    success_url=reverse_lazy("website:news-list")

class NewCreateView(CreateView):
    template_name="managenews/new-form.html"
    model=New
    form_class=NewForm
    success_url=reverse_lazy("website:news-list")




def contactus(request):
        
        if request.method=="POST":
            form = ContactForm(request.POST)  
            if form.is_valid():  
                form.save()  
                messages.success(request, "پیام شما با موفقیت ارسال شد .")  
                return redirect("/")  
        else:  
            messages.error(request, "پیام شما با خطا مواجه  شد")
def BreakingNewsLine():
    breaking_news = New.objects.filter(active=True,newstype='BREAKING').order_by('created_at')
    return breaking_news
def getSlider(mode):
    getNews=New.objects.filter(active=True,newstype=mode).order_by('-created_at')
    breakingSlider=[]
    for new in getNews:
        breakingSlider.append(
            {"imagesrc":f"{new.image.url}",
             "message":f"{new.brief_message}",
             "link":f"{new.slug}"}
             )
        
    return breakingSlider