from rest_framework import viewsets
from .models import Purchase
from .serializers import PurchaseSerializer
from django.shortcuts import get_object_or_404
from math import ceil
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from math import ceil
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class CalculatePointsView(APIView):
    """
    Retrieve and calculate points for a purchase.
    """
    @swagger_auto_schema(
        operation_description="Calculate points for a given purchase UUID",
        responses={200: 'Points calculation successful'}
    )
    def get(self, request, uuid, format=None):
        purchase = get_object_or_404(Purchase, uuid=uuid)
        total_points = 0

        total_points += sum(c.isalnum() for c in purchase.retailer)
        print("name: ",total_points)

        if purchase.total.endswith('.00'):
            print("no cent: ",purchase.total)
            total_points += 50

        if float(purchase.total) % 0.25 == 0:
            print("divisible by 0.25 :",purchase.total)
            total_points += 25

        total_points += 5 * (len(purchase.items.all()) // 2)


        for item in purchase.items.all():
            if len(item.shortDescription.strip()) % 3 == 0:
                total_points += ceil(float(item.price) * 0.2)


        if purchase.purchaseDate.day % 2 != 0:
            total_points += 6

        if purchase.purchaseTime.hour >= 14 and purchase.purchaseTime.hour < 16:
            total_points += 10

        return Response({'uuid': str(purchase.uuid), 'total_points': total_points}, status=status.HTTP_200_OK)


