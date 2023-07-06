from django.test import TestCase
from .models import Category, Exercise



class TestViews(TestCase):

    def setUp(self):
        print('Test start')

    def tearDown(self):
        print('Test finish')

    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        category = Category.objects.create(name='Все тело')
        exerise = Exercise.objects.create(name='Берпи', category=category)
        response = self.client.get('/')
        self.assertTrue('exerises' in response.context)



