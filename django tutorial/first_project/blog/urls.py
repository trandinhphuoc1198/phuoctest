
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='blog-home'),
    path('blog/create-post', views.create_post,name='create-post'),
    path('blog/<int:post_id>', views.view_post,name='view-post'),
    path('blog/<int:post_id>/edit', views.edit_post,name='edit-post'),
    path('blog/<int:post_id>/delete', views.delete_post,name='delete-post'),

]
