from django.contrib import admin
from .models import Article


class AdminArticle (admin.ModelAdmin):
    list_display = ('title','author','status')

admin.site.register(Article,AdminArticle)
# Register your models here.
