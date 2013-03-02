from django.contrib import admin

from .models import GroupPayment, Payment, Friend


class GroupPaymentAdmin(admin.ModelAdmin):
    """Custom admin for Payment."""
    list_display = ('user', 'title', 'value')

class FriendAdmin(admin.ModelAdmin):
    """Custom admin for Friend."""
    list_display = ('user', 'friend')

admin.site.register(GroupPayment, GroupPaymentAdmin)
admin.site.register(Payment)
admin.site.register(Friend, FriendAdmin)
