from django.contrib import admin

from articles.models import Article, Category, Tag, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    prepopulated_fields = ({'slug': ('title',)})
    filter_horizontal = ('tag',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'name', 'email', 'created_at')
    list_filter = ('created_at',)
    readonly_fields = list_filter
    search_fields = ('name', 'email')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
