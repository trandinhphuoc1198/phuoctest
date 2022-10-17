from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=1000)
    content=models.TextField(default='')
    created_date=models.DateTimeField(auto_now_add=True)
    edit_date=models.DateTimeField(auto_now=True)
    gerne=models.ManyToManyField('PostGerne')
    def __str__(self) -> str:
        return self.title
class Comment(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    place=models.ForeignKey(Post,on_delete=models.CASCADE)
    content=models.TextField(default='')
    created_date=models.DateTimeField(auto_now_add=True)
    edit_date=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.content[:10] if len(self.content)>=10 else self.content
class PostGerne(models.Model):
    gerne=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.gerne