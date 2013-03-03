from django.contrib import admin

from .models import GroupPayment, Payment, UserPayment, Friend, Group


class GroupPaymentAdmin(admin.ModelAdmin):
    """Custom admin for Payment."""
    list_display = ('user', 'title', 'value')

class UserPaymentAdmin(admin.ModelAdmin):
    """Custom admin for Payment."""
    list_display = ('from_user', 'to_user', 'value')

class FriendAdmin(admin.ModelAdmin):
    """Custom admin for Friend."""
    list_display = ('user', 'friend')

class GroupAdmin(admin.ModelAdmin):
    """Custom admin for Group."""
    list_display = ('user', 'title')

admin.site.register(GroupPayment, GroupPaymentAdmin)
admin.site.register(Payment)
admin.site.register(UserPayment, UserPaymentAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(Group, GroupAdmin)