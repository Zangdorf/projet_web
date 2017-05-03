from django.contrib import admin
from .models import Article, Stock


class StockInLine(admin.TabularInline):
    model = Stock


class ArticleAdmin(admin.ModelAdmin):
    fieldsets=[
        (None, {"fields":["name"]}),
        (None, {"fields":["department"]}),
        (None, {"fields":["description"]}),
        (None, {"fields":["price"]}),

    ]

    inlines = [StockInLine]
    list_display = ("name", "description","price", "get_quantity" , "department", "available", "get_date") #pour la vue general
    list_filter =["department", "name"] # we should filter by pub_date
    search_fields =["name", "description"]

admin.site.register(Article, ArticleAdmin)
