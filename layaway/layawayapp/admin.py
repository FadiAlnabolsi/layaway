from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import UserInfo, Artist, Events, TicketInfo, Ticket

# Register your models here.

class User_Info(admin.StackedInline):
    model = UserInfo
    can_delete = False
    verbose_name_plural = 'User_Info'

class UserAdmin(UserAdmin):
    inlines = (User_Info, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Artist)
admin.site.register(Events)
admin.site.register(TicketInfo)
admin.site.register(Ticket)
