from django.db import models  
from django.contrib.auth.models import User  
from django.utils.text import slugify  

class Category(models.Model):  
    title = models.CharField(max_length=50)  

    def __str__(self):  
        return self.title  


class Tag(models.Model):  
    title = models.CharField(max_length=50)  

    def __str__(self):  
        return self.title  


class New(models.Model):  
    journalist = models.ForeignKey(User, on_delete=models.CASCADE)  
    image = models.ImageField(upload_to="News/images/", default="News/images/default.jpg")  
    brief_message = models.CharField(max_length=50, null=True, blank=True)  
    title = models.CharField(max_length=255)  
    description = models.TextField()  
    categories = models.ManyToManyField(Category)  
    tags = models.ManyToManyField(Tag)  
    slug = models.SlugField(unique=True, null=False)  
    active = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def save(self, *args, **kwargs):  
        if not self.slug:  
            self.slug = slugify(self.title)  
        super().save(*args, **kwargs)  

    def __str__(self):  
        return self.title  

    class Meta:  
        verbose_name_plural = "News"