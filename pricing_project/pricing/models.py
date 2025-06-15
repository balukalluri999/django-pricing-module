from django.db import models

class PricingConfig(models.Model):
    name = models.CharField(max_length=100)
    days_active = models.JSONField(help_text="Days this config is active, e.g. ['Mon', 'Tue']")
    base_distance = models.FloatField(help_text="Base distance in KMs")
    base_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Base price for base distance")
    additional_price_per_km = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per KM after base distance")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Active: {self.is_active})"
