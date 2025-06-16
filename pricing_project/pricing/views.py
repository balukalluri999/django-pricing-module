from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PricingConfig
from datetime import datetime

class PriceCalculationView(APIView):
    def post(self, request):
        # Input: distance_km, ride_minutes, waiting_minutes, date
        data = request.data
        distance = float(data.get('distance_km', 0))
        ride_time = int(data.get('ride_minutes', 0))
        waiting_time = int(data.get('waiting_minutes', 0))
        date = data.get('date')  # e.g. "2025-06-15"

        day = datetime.strptime(date, "%Y-%m-%d").strftime("%a")  # Mon, Tue, etc.

        # Pick active config for the given day
        config = PricingConfig.objects.filter(is_active=True, days_active__contains=[day]).first()
        if not config:
            return Response({"error": "No active config found for this day"}, status=404)

        # Distance Calculation
        if distance <= config.base_distance:
            distance_cost = config.base_price
        else:
            additional_km = distance - config.base_distance
            distance_cost = config.base_price + (additional_km * float(config.additional_price))

        # Time Multiplier Calculation
        multiplier = 1.0
        for tm in config.time_multipliers.all():
            if tm.min_minutes <= ride_time <= tm.max_minutes:
                multiplier = tm.multiplier
                break

        time_cost = distance_cost * multiplier

        # Waiting Charge
        wc_obj = config.waiting_charges.first()
        waiting_cost = 0
        if wc_obj and waiting_time > wc_obj.free_minutes:
            extra_wait = waiting_time - wc_obj.free_minutes
            waiting_cost = extra_wait * float(wc_obj.charge_per_min)

        final_price = round(time_cost + waiting_cost, 2)

        return Response({"final_price": final_price})
