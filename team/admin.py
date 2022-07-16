from django.contrib import admin

from team.models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name', 'author_comment', 'profession']
    list_filter = ['id', 'author_name']


admin.site.register(Team, TeamAdmin)
