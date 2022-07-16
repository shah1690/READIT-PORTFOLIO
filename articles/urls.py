from django.urls import path

from articles.views import home_view, single_view, blog_view

urlpatterns = [
    path('', home_view),
    path('index.html/', home_view, name='home'),
    path('blog-single.html/<slug:slug>', single_view, name='single'),
    path('blog.html/', blog_view, name='blog'),

]
