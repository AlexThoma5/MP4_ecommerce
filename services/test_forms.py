from django.test import TestCase
from .forms import ServiceForm


class TestServiceForm(TestCase):

    def test_form_is_valid_with_all_required_fields(self):
        """Form should be valid when all required fields are provided"""
        form_data = {
            'service_type': 1,
            'name': 'Physiotherapy',
            'description': 'This is a test description',
            'price': 45,
            'duration': 60,
            'session_count': 5,
        }
        form = ServiceForm(form_data)
        self.assertTrue(
            form.is_valid(), msg='Form is not valid with all required fields')

    def test_form_is_invalid_without_service_type(self):
        """Form should be invalid if service_type is missing"""
        form_data = {
            'service_type': None,
            'name': 'Physiotherapy',
            'description': 'This is a test description',
            'price': 45,
            'duration': 60,
            'session_count': 5,
        }
        form = ServiceForm(form_data)
        self.assertFalse(
            form.is_valid(), msg='Form is valid without service_type')

    def test_form_is_invalid_without_name(self):
        """Form should be invalid if name is missing"""
        form_data = {
            'service_type': 1,
            'name': '',
            'description': 'This is a test description',
            'price': 45,
            'duration': 45,
            'session_count': 1,
        }
        form = ServiceForm(form_data)
        self.assertFalse(
            form.is_valid(), msg='Form is valid without duration')

    def test_form_is_invalid_without_description(self):
        """Form should be invalid if name is missing"""
        form_data = {
            'service_type': 1,
            'name': 'test',
            'description': '',
            'price': 45,
            'duration': 45,
            'session_count': 1,
        }
        form = ServiceForm(form_data)
        self.assertFalse(
            form.is_valid(), msg='Form is valid without description')

    def test_form_is_invalid_without_price(self):
        """Form should be invalid if price is missing"""
        form_data = {
            'service_type': 1,
            'name': 'test',
            'description': 'This is a test description',
            'price': None,
            'duration': 45,
            'session_count': 1,
        }
        form = ServiceForm(form_data)
        self.assertFalse(
            form.is_valid(), msg='Form is valid without price')

    def test_form_is_invalid_without_duration(self):
        """Form should be invalid if duration is missing"""
        form_data = {
            'service_type': 1,
            'name': 'Physiotherapy',
            'description': 'This is a test description',
            'price': 45,
            'duration': None,
            'session_count': 5,
        }
        form = ServiceForm(form_data)
        self.assertFalse(
            form.is_valid(), msg='Form is valid without duration')

    def test_form_is_invalid_without_session_count(self):
        """Form should be invalid if session_count is missing"""
        form_data = {
            'service_type': 1,
            'name': 'Physiotherapy',
            'description': 'This is a test description',
            'price': 45,
            'duration': 60,
            'session_count': None,
        }
        form = ServiceForm(form_data)
        self.assertFalse(
            form.is_valid(), msg='Form is valid without session_count')
