from django.urls import path
from .views import PriceCalculationView, PricingConfigCreateView

urlpatterns = [
    path('calculate-price/', PriceCalculationView.as_view(), name='calculate-price'),
    path('config/create/', PricingConfigCreateView.as_view(), name='config-create'),
]
