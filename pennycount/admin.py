from django.contrib import admin

from .models import Payment, Friend


class PaymentAdmin(admin.ModelAdmin):
    """Custom admin for Payment."""
    list_display = ('user', 'title', 'value')

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Friend)
