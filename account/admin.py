from django.contrib import admin
from .models import CustomUser, Admin, Seller, UserProfile

# Admin model for User
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role')
    search_fields = ('username', 'email', 'first_name', 'last_name')

# Admin model for Seller
class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'seller_status', 'account_create_time')
    search_fields = ('user__username', 'user__email')
    list_filter = ('seller_status',)

# Admin model for UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email')

# Register models with the admin site
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Admin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
