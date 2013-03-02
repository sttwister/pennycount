from django.contrib import admin

from .models import Payment, Friend


class PaymentAdmin(admin.ModelAdmin):
    """Custom admin for Payment."""
    list_display = ('user', 'title', 'value')

class FriendAdmin(admin.ModelAdmin):
    """Custom admin for Friend."""
    list_display = ('user', 'friend')

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Friend, FriendAdmin)
