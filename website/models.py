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

    NEWS_TYPE_CHOICES = [
        ('BREAKING', 'Breaking News'),  # اخبار فوری
        ('DEVELOPING', 'Developing Story'),  # خبر در حال تکامل
        ('URGENT', 'Urgent'),  # فوری
        ('LIVE', 'Live Updates'),  # به‌روزرسانی‌های زنده
        ('EXCLUSIVE', 'Exclusive'),  # انحصاری
    ]

    journalist = models.ForeignKey(User, on_delete=models.CASCADE)  
    image = models.ImageField(upload_to="news/images/", default="news/images/default.svg")  
    brief_message = models.CharField(max_length=50, null=True, blank=True)  
    title = models.CharField(max_length=255)  
    description = models.TextField()  
    categories = models.ManyToManyField(Category)  
    tags = models.ManyToManyField(Tag)  
    slug = models.SlugField(unique=True, allow_unicode=True,null=True,blank=True)   
    newstype = models.CharField(max_length=20, choices=NEWS_TYPE_CHOICES,null=True, blank=True) 
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






class Contact(models.Model):
    firstName=models.CharField(max_length=255)
    lastName=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    description=models.TextField()

    active=models.BooleanField(default=False,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):  
        return self.email  

    class Meta:  
        verbose_name_plural = "Contacts"