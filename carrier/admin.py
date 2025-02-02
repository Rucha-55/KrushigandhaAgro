from django.contrib import admin
from carrier.models import Carrier

# Custom admin class for the Carrier model
class CarrierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'experience', 'gender', 'city', 'resume')  # Fields to display in the list view
    search_fields = ('name', 'email', 'post')  # Fields you can search by in the admin
    list_filter = ('post', 'gender')  # Filters for filtering by post and gender

# Register the Carrier model with the custom admin class
admin.site.register(Carrier, CarrierAdmin)
