
from rest_framework import generics
from .models import Food
from .serializers import FoodListSerializer




class FoodApiView(generics.ListAPIView):
    queryset = Food.objects.all().filter(category_id__gt=0, is_publish=True)
    serializer_class = FoodListSerializer