from django.contrib import admin
from .models import Brand, Phone


# Register your models here.
class PhoneAdmin(admin.ModelAdmin):
    list_display = ["phone_model", "phone_brand", "is_available"]
    list_filter = ["is_available"]
    list_editable = ["is_available"]
    search_fields = ["phone_model", "phone_brand"]

admin.site.register(Brand)
admin.site.register(Phone, PhoneAdmin)
