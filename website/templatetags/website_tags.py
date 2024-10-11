from django import template
register = template.Library()
from website.models import  New
from datetime import datetime 


@register.inclusion_tag("website/includes/latest-news.html")
def recent_news():
    News=New.objects.filter(active=True).order_by("-updated_at")[:4]
    return {"News":News}

