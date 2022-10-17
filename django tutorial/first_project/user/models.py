from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
    change_times=models.IntegerField(default=0)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nick_name=models.CharField(default='Anonymous',max_length=100)
    gender=models.CharField(default='Undentify',max_length=10,
        choices=[('Undentify','Undentify'),('Male','Male'),('Female','Female')],verbose_name='Sex')
    birthday=models.DateField(blank=True,null=True)
    image=models.ImageField(default='default.png',upload_to='profile')

    def save(self,*args,**kwargs):
        if self.user is not None and self.change_times==0:
            if self.user.first_name != '':
                self.nick_name=self.user.first_name
            else:
                self.nick_name=self.user.username
        self.change_times+=1
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.height >300 or img.width>300:
            img.thumbnail((300,300))
            img.save(self.image.path)

    def __str__(self) -> str:
        return f'{self.user}\'s profile'