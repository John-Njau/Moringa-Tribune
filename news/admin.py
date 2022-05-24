from django.contrib import admin
from .models import Editor,Article,tags

# Register your models here.
# allows us to customize models on the admin page
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Editor)
admin.site.register(Article, ArticleAdmin)
admin.site.register(tags)