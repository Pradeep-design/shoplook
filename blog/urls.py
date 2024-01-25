from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="blogHome"),
    path('blogComment', views.blogComment, name="blogComment"),
    path('blogpost/<int:id>', views.blogpost, name="blogHome"),
    #path('BlogPostLike/<int:pk>',views.BlogPostLike , name="BlogPostLike"),
    path('like/<int:post_id>',views.like,name='like'),
    path('blog_create/', views.blog_create, name="blog_create"),
    path('blogCommentUpdate/<int:sno>', views.blogCommentUpdate, name="blog_comment_update"),
    path('blog_delete/<int:post_id>', views.blog_delete, name="blog_delete"),
]

