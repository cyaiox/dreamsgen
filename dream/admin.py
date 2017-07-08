from django.contrib import admin
from .models import Group, Dream, Frame, Pack


# Register your models here.
admin.site.register(Group)

class FrameInline(admin.StackedInline):
    model = Frame
    extra = 1


class DreamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'group', 'is_available')
    inlines = [FrameInline]
admin.site.register(Dream, DreamAdmin)

admin.site.register(Pack)