from django.contrib import admin
from .models import Purchase, Item

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1  # Number of empty forms to display

class PurchaseAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ('uuid', 'retailer', 'purchaseDate', 'purchaseTime', 'total')
    search_fields = ['retailer', 'total']

admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Item)  # You can also customize the Item admin if needed
