from django.test import TestCase
from datetime import date
from django.contrib.auth.models import User
from checkout.models import Order, Coupon

class CouponModelTest(TestCase):
    """ Test Coupon Model """

    def test_coupon_str(self):
        # Create Coupon Code
        coupon = Coupon.objects.create(
            code='test',
            discount=20,
            active=True,
            start_date=date(2023, 6, 1),
            expiry_date=date(2023, 6, 30)
        )

        # Assert Coupon Code is the correct string
        self.assertEqual(str(coupon), 'test')


class OrderModelTest(TestCase):
    """ Test Order Model """

    def setUp(self):
        # Create User
        self.user = User.objects.create_user(
            username='regularuser',
            password='testpw',
        )

        # Create Order
        self.order = Order.objects.create(
            order_number='1234567890',
            full_name='Test User',
            email='testuser@email.com',
            phone_number='12345678',
            country='IE',
            postcode='12345',
            town_or_city='Dublin',
            street_address1='Street',
            county='Dublin',
        )

    def test_order_fields(self):
        # Assert Order Fields are Correct
        
        self.assertEqual(self.order.order_number, '1234567890')
        self.assertEqual(self.order.full_name, 'Test User')
        self.assertEqual(self.order.email, 'testuser@email.com')
        self.assertEqual(self.order.phone_number, '12345678')
        self.assertEqual(self.order.country, 'IE')
        self.assertEqual(self.order.postcode, '12345')
        self.assertEqual(self.order.town_or_city, 'Dublin')
        self.assertEqual(self.order.street_address1, 'Street')
        self.assertEqual(self.order.county, 'Dublin')