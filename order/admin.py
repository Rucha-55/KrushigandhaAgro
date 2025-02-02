from django.contrib import admin
from order.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'quantity', 'address', 'phone', 'whatsapp', 'created_at')
    search_fields = ('product_name', 'phone', 'whatsapp')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(Order, OrderAdmin)

