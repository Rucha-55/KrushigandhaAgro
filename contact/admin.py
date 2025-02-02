from django.contrib import admin
from contact.models import Contact

class ContactAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('username', 'email', 'mobile', 'created_at')

    # Optional: Add search and filter functionality
    search_fields = ('username', 'email', 'mobile')  # Enables a search bar for these fields
    list_filter = ('created_at',)  # Adds filter options by creation date

admin.site.register(Contact, ContactAdmin)
