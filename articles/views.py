from django.shortcuts import render, redirect, get_object_or_404

from articles.forms import CreateCommentForm
from articles.models import Article, Tag, Category, Comment


def home_view(request):
    articles = Article.objects.all()
    last_news = Article.objects.order_by('-id')[:3]
    search = request.GET.get('search')
    if search:
        articles = articles.filter(title__icontains=search)
    ctg = request.GET.get('ctg')
    if ctg:
        articles = articles.filter(category__category__exact=ctg)
    tag = request.GET.get('tag')
    if tag:
        articles = articles.filter(tag__tag__exact=tag)
    ctx = {
        'articles': articles,
        'last_news': last_news,
        'search': search,

    }
    return render(request, 'index.html', ctx)


def single_view(request, slug):
    obj = Article.objects.get(slug=slug)
    category = Category.objects.all()
    last_3_articles = Article.objects.order_by('-id')[:3]
    last_news = Article.objects.order_by('-id')[:3]
    tags = Tag.objects.all()
    comments = Comment.objects.order_by('-id')[:3]
    form = CreateCommentForm(request.POST or None, request.FILES)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = obj
        comment.save()
    ctx = {
        'objects': obj,
        'categorys': category,
        'last_3_articles': last_3_articles,
        'tags': tags,
        'comments': comments,
        'form': form,
        'last_news': last_news,

    }
    return render(request, 'blog-single.html', ctx)


def blog_view(request):
    article = Article.objects.all()
    last_news = Article.objects.order_by('-id')[:3]
    ctx = {
        'article': article,
        'last_news': last_news,
    }
    return render(request, 'blog.html', ctx)
