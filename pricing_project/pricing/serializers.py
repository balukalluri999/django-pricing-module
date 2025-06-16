from rest_framework import serializers
from .models import PricingConfig, TimeMultiplier, WaitingCharge

class TimeMultiplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeMultiplier
        fields = '__all__'

class WaitingChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingCharge
        fields = '__all__'

class PricingConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingConfig
        fields = '__all__'
