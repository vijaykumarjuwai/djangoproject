from django.contrib import admin
from .models import Articles

# Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'publish')
    list_filter = ('status', 'created', 'updated')
    search_fields = ['title']


admin.site.register(Articles, ArticlesAdmin)