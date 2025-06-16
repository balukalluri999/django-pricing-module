from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PricingConfig
from datetime import datetime
import logging
from rest_framework import generics
from .serializers import PricingConfigSerializer

logger = logging.getLogger(__name__)

class PriceCalculationView(APIView):
    def get(self, request):
        return self.calculate_price(request.query_params)

    def post(self, request):
        return self.calculate_price(request.data)

    def calculate_price(self, data):
        required_fields = ['distance_km', 'ride_minutes', 'waiting_minutes', 'date']
        missing = [field for field in required_fields if not data.get(field)]

        if missing:
            return Response({"error": f"Missing required fields: {', '.join(missing)}"}, status=400)

        try:
            logger.info(f"📥 Received Data: {data}")

            distance = float(data.get('distance_km'))
            ride_time = int(data.get('ride_minutes'))
            waiting_time = int(data.get('waiting_minutes'))
            date = data.get('date')

            logger.info(f"📆 Date received: {date}")
            day = datetime.strptime(date, "%Y-%m-%d").strftime("%a")  # 'Sun', 'Mon', etc.
            logger.info(f"🗓 Day: {day}")

            config = PricingConfig.objects.filter(is_active=True, days_active__icontains=day).first()
            if not config:
                return Response({"error": f"No active config found for {day}"}, status=404)

            # Step 1: Distance-based cost
            if distance <= config.base_distance:
                distance_cost = config.base_price
            else:
                extra_km = distance - config.base_distance
                distance_cost = config.base_price + (extra_km * float(config.additional_price_per_km))

            # Step 2: Apply time multiplier
            multiplier = 1.0
            for tm in config.time_multipliers.all():
                if tm.min_minutes <= ride_time <= tm.max_minutes:
                    multiplier = tm.multiplier
                    break

            time_cost = distance_cost * multiplier

            # Step 3: Apply waiting time charge
            waiting_cost = 0
            wc = config.waiting_charges.first()
            if wc and waiting_time > wc.free_minutes:
                extra_wait = waiting_time - wc.free_minutes
                waiting_cost = extra_wait * float(wc.charge_per_min)

            # Final Price
            final_price = round(time_cost + waiting_cost, 2)

            return Response({"final_price": final_price})

        except Exception as e:
            logger.exception("Error calculating price")
            return Response({"error": str(e)}, status=400)
class PricingConfigCreateView(generics.CreateAPIView):
    queryset = PricingConfig.objects.all()
    serializer_class = PricingConfigSerializer