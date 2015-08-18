from django.contrib import admin

# Register your models here.
from collection.models import PrivateLabel

class PrivateLabelAdmin(admin.ModelAdmin):
    model = PrivateLabel
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(PrivateLabel, PrivateLabelAdmin)