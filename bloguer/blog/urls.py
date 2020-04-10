from django.urls import path
from .views import BlogListView, BlogDetailView


blogs_patterns = ([
    path('blog/', BlogListView.as_view(), name="blogs"),
    path('<int:pk>/<slug:blog_slug>/', BlogDetailView.as_view(), name="blog"),

], 'blogs')
