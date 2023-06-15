from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile


class UserProfileModelTest(TestCase):
    """
    Test for the UserProfile model
    """

    @classmethod
    def setUpTestData(cls):
        # Create a test User
        cls.user = User.objects.create_user(username="testuser", password="testpass")

    def test_user_profile_creation(self):
        # Retrieve the UserProfile object for the user, or create a new one if it doesn't exist
        try:
            user_profile = UserProfile.objects.get(user=self.user)
        except UserProfile.DoesNotExist:
            user_profile = UserProfile(user=self.user)

        # Set the attributes of the UserProfile object
        user_profile.name = "Test User"
        user_profile.default_phone_number = "123456789"
        user_profile.default_street_address1 = "123 Test Street"
        user_profile.default_street_address2 = "Street 1"
        user_profile.default_town_or_city = "Test City"
        user_profile.default_county = "Test County"
        user_profile.default_postcode = "12345"
        user_profile.default_country = "IE"
        user_profile.save()

        # Retrieve the UserProfile object from the database
        stored_user_profile = UserProfile.objects.get(id=user_profile.id)

        # Assert that the stored UserProfile object matches the created object
        self.assertEqual(stored_user_profile.user, self.user)
        self.assertEqual(stored_user_profile.name, "Test User")
        self.assertEqual(stored_user_profile.default_phone_number, "123456789")
        self.assertEqual(stored_user_profile.default_street_address1, "123 Test Street")
        self.assertEqual(stored_user_profile.default_street_address2, "Street 1")
        self.assertEqual(stored_user_profile.default_town_or_city, "Test City")
        self.assertEqual(stored_user_profile.default_county, "Test County")
        self.assertEqual(stored_user_profile.default_postcode, "12345")
        self.assertEqual(stored_user_profile.default_country, "IE")

    def test_user_profile_string_representation(self):
        # Retrieve the UserProfile object for the user, or create a new one if it doesn't exist
        try:
            user_profile = UserProfile.objects.get(user=self.user)
        except UserProfile.DoesNotExist:
            user_profile = UserProfile(user=self.user)

        # Assert that the string representation of the UserProfile object is the username of the associated user
        self.assertEqual(str(user_profile), self.user.username)
