from django import template
register = template.Library()
from website.models import  New,Category
from datetime import datetime 


@register.inclusion_tag("website/includes/latest-news.html")
def recent_news():
    News=New.objects.filter(active=True).order_by("-updated_at")[:4]
    return {"News":News}

@register.simple_tag()
def getCat():
    categories=Category.objects.all()
    new=New.objects.all(active=True)
    categories_count={}
    for cat in categories:
        categories_count[cat]=new.filter(category__title=cat).count()
    
    return {'categories_count':categories_count}