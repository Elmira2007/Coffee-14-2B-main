from django.contrib import admin
from apps.contacts.models import  Contacts
# Register your models here.

class ContactsFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', 'email')
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    readonly_fields = ('massage', 'email', 'name', 'subject', )
    
admin.site.register(Contacts, ContactsFilterAdmin)