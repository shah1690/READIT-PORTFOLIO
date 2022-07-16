from django.shortcuts import render
from.form import ContactForm
from articles.models import Article
from contact.models import Contact


def contact_view(request):
    cts = Contact.objects.all()
    last_news = Article.objects.order_by('-id')[:3]
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    ctx = {
        'cts': cts,
        'last_news': last_news,
        'form': form
    }
    return render(request, 'contact.html', ctx)
