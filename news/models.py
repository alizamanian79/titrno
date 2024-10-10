from django.db import models
from users.models import CustomUser
# Create your models here.


class journalist(models.Model):
    # user_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True),
    image=models.ImageField( upload_to='journalist/', default="journalist/default.jpg" ,null=True),
    name=models.CharField(max_length=255),
    lastName=name=models.CharField(max_length=255),
    active=models.BooleanField(default=False),
    created_at=models.DateTimeField(auto_now_add=True),
    updated_at=models.DateTimeField(auto_now=True),

    def __str__(self):
        return self.name
    

# class News(models.Model):
#     journalist_id=models.ForeignKey(journalist, on_delete=models.CASCADE)
#     image=models.ImageField( upload_to='news/', default="news/default.jpg" ,null=True)
#     brief_message=models.CharField(max_length=50)
#     title=models.CharField(max_length=255),
#     description=models.TextField(),
#     publish_at=models.DateTimeField(auto_now_add=True),
#     edited_at=models.DateTimeField(auto_now=True),

    