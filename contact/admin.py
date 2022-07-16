from django.contrib import admin

from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message']
    list_filter = ['id', 'name']


admin.site.register(Contact, ContactAdmin)
