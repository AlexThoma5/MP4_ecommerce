from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_form_is_valid_with_all_fields(self):
        """Test all fields"""
        contact_form = ContactForm(
            {
                'full_name': 'Alex Test',
                'email': 'test@gmail.com',
                'phone_number': '1234567890',
                'subject': 1,
                'message': 'How much is this test?',
            }
        )
        self.assertTrue(contact_form.is_valid(),
                        msg='Form is not valid with all fields complete')

    def test_form_is_invalid_without_full_name(self):
        """Form should be invalid if full_name is missing"""
        form = ContactForm({
            'full_name': '',
            'email': 'john@example.com',
            'phone_number': '07123456789',
            'subject': 1,
            'message': 'I would like more information.'
        })
        self.assertFalse(
            form.is_valid(), msg='Form is valid without full_name')

    def test_form_is_invalid_without_email(self):
        """Form should be invalid if email is missing"""
        form = ContactForm({
            'full_name': 'John Smith',
            'email': '',
            'phone_number': '07123456789',
            'subject': 1,
            'message': 'I would like more information.'
        })
        self.assertFalse(form.is_valid(), msg='Form is valid without email')

    def test_form_is_invalid_without_message(self):
        """Form should be invalid if message is missing"""
        form = ContactForm({
            'full_name': 'John Smith',
            'email': 'john@example.com',
            'phone_number': '07123456789',
            'subject': 1,
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg='Form is valid without message')
