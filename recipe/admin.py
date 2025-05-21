from django.contrib import admin
from .models import Recipe, Category


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
