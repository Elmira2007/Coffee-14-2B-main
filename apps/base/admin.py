from django.contrib import admin
from django.contrib.auth.models import User, Group

from apps.base.models import InfoUser,Secondary,Testim

class InfoUserFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', 'phone')
    list_display = ('name', 'work', 'age')
    search_fields = ('name', )

admin.site.register(InfoUser, InfoUserFilterAdmin)
admin.site.register(Secondary)
admin.site.register(Testim)
admin.site.unregister(User)
admin.site.unregister(Group)
