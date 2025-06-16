from django.db import models
from django.contrib.auth.models import User

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
    
class TimeMultiplier(models.Model):
    config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE, related_name='time_multipliers')
    min_minutes = models.PositiveIntegerField()
    max_minutes = models.PositiveIntegerField()
    multiplier = models.FloatField()

    def __str__(self):
        return f"{self.multiplier}x for {self.min_minutes}-{self.max_minutes} min"


class WaitingCharge(models.Model):
    config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE, related_name='waiting_charges')
    free_minutes = models.PositiveIntegerField()
    charge_per_min = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.charge_per_min}/min after {self.free_minutes} min"

class ConfigChangeLog(models.Model):
    config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=[('create', 'Create'), ('update', 'Update'), ('delete', 'Delete')])
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.config.name} - {self.action} by {self.performed_by}"