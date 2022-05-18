from django.contrib import admin
from portapp.models import *

# Register your models here.
admin.site.register(Education)
admin.site.register(Contact)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_diplay = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'comment')

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_diplay = [
        'title',
        'image',
        'poster'
    ]