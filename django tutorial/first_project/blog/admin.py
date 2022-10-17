from django.contrib import admin
from .models import Post,PostGerne,Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(PostGerne)
admin.site.register(Comment)