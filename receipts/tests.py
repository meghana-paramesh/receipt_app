from django.test import TestCase
from django.urls import reverse
from .models import Purchase, Item
from datetime import datetime
from django.utils import timezone

class PointsCalculationTests(TestCase):
    def setUp(self):
        # Create a Purchase instance
        self.purchase = Purchase.objects.create(
            retailer='TestShop',
            purchaseDate=timezone.now().date(),
            purchaseTime=datetime.now().time(),
            total='100.00'
        )
        # Create some Item instances
        for i in range(4):
            Item.objects.create(
                purchase=self.purchase,
                shortDescription='Item {}'.format(i),
                price='10.00'
            )

    def test_retailer_name_points(self):
        self.purchase.retailer = 'Shop123'
        self.purchase.save()
        response = self.client.get(reverse('calculate-points', args=[self.purchase.uuid]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['total_points'], 7)  # 7 alphanumeric characters

    def test_total_round_dollar(self):
        self.purchase.total = '100.00'
        self.purchase.save()
        response = self.client.get(reverse('calculate-points', args=[self.purchase.uuid]))
        self.assertEqual(response.status_code, 200)
        self.assertIn('total_points', response.json())
        self.assertEqual(response.json()['total_points'], 50)  # 50 points for round dollar


    def test_odd_day_points(self):
        self.purchase.purchaseDate = datetime(2021, 1, 1).date()  # An odd day
        self.purchase.save()
        response = self.client.get(reverse('calculate-points', args=[self.purchase.uuid]))
        self.assertEqual(response.status_code, 200)
        self.assertIn('total_points', response.json())
        self.assertEqual(response.json()['total_points'], 6)  # 6 points for odd day

