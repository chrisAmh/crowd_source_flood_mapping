from django.test import TestCase

# Create your tests here.

from .models import FloodImage

class FloodImageModelTest(TestCase):
    def setUp(self):
        FloodImage.objects.create(title="Test Flood", latitude=0, longitude=0)

    def test_flood_image_creation(self):
        flood_image = FloodImage.objects.get(title="Test Flood")
        self.assertEqual(flood_image.title, "Test Flood")
