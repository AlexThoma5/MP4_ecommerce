from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_form_is_valid_with_all_fields(self):
        """Form should be valid when all fields are provided"""
        form = OrderForm({
            'full_name': 'Alice Test',
            'email': 'alice@example.com',
            'phone_number': '07123456789',
        })
        self.assertTrue(
            form.is_valid(), msg='Form is not valid with all fields')

    def test_form_is_invalid_without_full_name(self):
        """Form should be invalid if full_name is missing"""
        form = OrderForm({
            'full_name': '',
            'email': 'alice@example.com',
            'phone_number': '07123456789',
        })
        self.assertFalse(
            form.is_valid(), msg='Form is valid without full_name')

    def test_form_is_invalid_without_email(self):
        """Form should be invalid if email is missing"""
        form = OrderForm({
            'full_name': 'Alice Test',
            'email': '',
            'phone_number': '07123456789',
        })
        self.assertFalse(
            form.is_valid(), msg='Form is valid without email')

    def test_form_is_invalid_without_phone_number(self):
        """Form should be invalid if phone_number is missing"""
        form = OrderForm({
            'full_name': 'Alice Test',
            'email': 'alice@example.com',
            'phone_number': '',
        })
        self.assertFalse(
            form.is_valid(), msg='Form is valid without phone_number')
