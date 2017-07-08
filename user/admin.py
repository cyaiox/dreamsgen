from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Address, Log, WishList, Experience


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 1
    max_num = 1


class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)
        UserAdmin.inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Address)
admin.site.register(Log)
admin.site.register(WishList)
admin.site.register(Experience)