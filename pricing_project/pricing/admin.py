from django.contrib import admin
from .models import PricingConfig
from .models import PricingConfig, TimeMultiplier, WaitingCharge
from .models import ConfigChangeLog
from .signals import set_current_user

@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_distance', 'base_price', 'is_active', 'created_at')
    list_filter = ('is_active', 'days_active')
    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        set_current_user(request.user)
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        set_current_user(request.user)
        super().delete_model(request, obj)

    
@admin.register(ConfigChangeLog)
class ConfigChangeLogAdmin(admin.ModelAdmin):
    list_display = ('config', 'action', 'performed_by', 'timestamp')
    list_filter = ('action', 'performed_by')

admin.site.register(TimeMultiplier)
admin.site.register(WaitingCharge)