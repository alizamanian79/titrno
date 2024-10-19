from django import template
register = template.Library()
from website.models import  New,Category,Tag
from datetime import datetime 
from ..forms import ContactForm
from django.contrib import messages
from django.shortcuts import redirect

@register.inclusion_tag("website/includes/latest-news.html")
def recent_news():
    News=New.objects.filter(active=True).order_by("-updated_at")[:4]
    return {"News":News}




@register.inclusion_tag("footer.html")
def footer():
    allcategories=Category.objects.all()
    new=New.objects.all()
    categories_count={}
    tags_count={}
    alltags=Tag.objects.all()

    for cat in allcategories:
        categories_count[cat]=new.filter(categories__title=cat).count()
    
    for tag in alltags:
        tags_count[tag]=new.filter(tags__title=tag).count()
    
    return {'categories_count':categories_count,"tags_count":tags_count}
    





@register.inclusion_tag("contact.html")  
def contact():   
    return   