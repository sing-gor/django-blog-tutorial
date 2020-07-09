from django.contrib import admin
from controllers.articles import models
# Register your models here.
@admin.register(models.Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time',)
