from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class PricingConfig(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    base_price = models.FloatField()
    base_distance = models.FloatField()
    additional_price_per_km = models.FloatField(default=0.0)
    days_active = ArrayField(models.CharField(max_length=10), blank=True, default=list)    
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