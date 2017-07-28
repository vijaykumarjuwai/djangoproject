from django.contrib import admin
from .models import Article

'''
class ArticleAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Article
        exclude = ('',)

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'publish')
    list_filter = ('status', 'created', 'updated')
    search_fields = ['title']
    form = ArticleAdminForm
'''

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'publish')
    list_filter = ('status', 'created', 'updated')
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)