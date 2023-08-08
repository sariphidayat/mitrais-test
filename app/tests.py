from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.validators import ValidationError

from app.models import User
from app.serializers import UserSerializer


class UserTestCase(APITestCase):
    url = '/api/users/'
    valid_data = {
        'mobile_number': '08123456789',
        'first_name': 'John',
        'last_name': 'Doe',
        'date_of_birth': '1999-04-20',
        'sex': True,
        'email': 'john.doe@gmail.com'
    }

    def test_skip_required_fields(self):
        data = {
            'date_of_birth': '2000-04-20',
            'sex': True
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        err_message = "This field is required."
        with self.assertRaisesMessage(ValidationError, err_message):
            serializer = UserSerializer(data=data)
            serializer.is_valid(raise_exception=True)
        required_fields = ['mobile_number', 'first_name', 'last_name', 'email']
        for f in required_fields:
            self.assertIn(f, serializer.errors)

    def test_valid_id_mobile_number(self):
        invalid_mobile_numbers = [
            '07284645321',  # doesn't start with '08' or '628'
            '082846453',  # the length is less than 10
            '6282846453',  # the length is less than 11
            '6282abcdevc',  # alphanumeric
        ]

        for number in invalid_mobile_numbers:
            data = {
                'mobile_number': number,
            }
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            err_message = "Please enter a valid Indonesian mobile number."
            with self.assertRaisesMessage(ValidationError, err_message):
                serializer = UserSerializer(data=data)
                serializer.is_valid(raise_exception=True)
            self.assertIn("mobile_number", serializer.errors)

    def test_unique_mobile_number(self):
        response = self.client.post(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        err_message = "User with this Mobile Number already exists."
        with self.assertRaisesMessage(ValidationError, err_message):
            serializer = UserSerializer(data=self.valid_data)
            serializer.is_valid(raise_exception=True)

        self.assertIn("mobile_number", serializer.errors)
        User.objects.get(
            mobile_number=self.valid_data['mobile_number']).delete()

    def test_unique_email(self):
        response = self.client.post(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        err_message = "User with this Email already exists."
        with self.assertRaisesMessage(ValidationError, err_message):
            serializer = UserSerializer(data=self.valid_data)
            serializer.is_valid(raise_exception=True)

        self.assertIn("email", serializer.errors)
        User.objects.get(email=self.valid_data['email']).delete()
