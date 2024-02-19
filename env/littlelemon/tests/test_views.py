from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Pizza", Price=150, Inventory=50)
        Menu.objects.create(Title="Burger", Price=120, Inventory=75)

    def test_getall(self):
        client = APIClient()
        url = reverse('menu')
        response = client.get(url)
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)