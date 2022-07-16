from django.shortcuts import render

from articles.models import Article
from team.models import Team


def team_view(request):
    team = Team.objects.all()
    creators = Team.objects.all()
    last_news = Article.objects.order_by('-id')[:2]
    ctx = {
        'team': team,
        'creators': creators,
        'last_news': last_news,
    }
    return render(request, 'about.html', ctx)
