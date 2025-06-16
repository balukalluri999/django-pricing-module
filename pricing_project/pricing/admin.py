from django.contrib import admin
from .models import PricingConfig
from .models import PricingConfig, TimeMultiplier, WaitingCharge


@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_distance', 'base_price', 'is_active', 'created_at')
    list_filter = ('is_active', 'days_active')
    search_fields = ('name',)

admin.site.register(TimeMultiplier)
admin.site.register(WaitingCharge)