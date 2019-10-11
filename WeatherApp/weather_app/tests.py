from django.test import TestCase
from .models import City
from django.urls import reverse

# Create your tests here.
class CityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        City.objects.create(City="Sokoto")
    
    def test_city_name_label(self):
        city = City.objects.get(id=1)
        field_label = city._meta.get_field('City').verbose_name
        self.assertEquals(field_label, 'City')
    
    def test_city_name_length(self):
        city = City.objects.get(id=1)
        field_length = city._meta.get_field('City').max_length
        self.assertEqual(field_length, 40)

    def test_object_name_is_city_name(self):
        city = City.objects.get(id=1)
        expected_object_name = f'{city.City}'
        self.assertEqual(expected_object_name, str(city))
    
    # def test_object_url(self):
    #     city = City.objects.get(id=1)
    #     self.assertEqual(city.get_absolute_url(), f'/{city.City}')

