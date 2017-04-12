from django.contrib import admin
from .models import Article, Stock


class StockInLine(admin.TabularInline):
    model = Stock


class ArticleAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{"fields":["name"]}),
        (None, {"fields":["department"]}),
        (None, {"fields":["description"]}),
        (None, {"fields":["price"]}),

    ]

    def get_quantity(self, obj):
        return obj.stock.quantity
    get_quantity.admin_order_field = "quantity"
    get_quantity.short_description="Remaining Stock"

    inlines=[StockInLine]
    list_display = ("name", "description","price", 'get_quantity' , "department") #pour la vue general
    list_filter=["name"] # we should filter by pub_date
    search_fields=["nom", "description"]

admin.site.register(Article, ArticleAdmin)
