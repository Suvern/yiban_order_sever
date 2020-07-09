from django.contrib import admin
from .models import *

admin.site.register(Token)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'unit', 'content', 'state', 'person')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'unit', 'position', 'admin_type')


title = 'CUMT易班大厅预约管理后台'

admin.site.site_title = title
admin.site.site_header = title
admin.site.index_title = title
