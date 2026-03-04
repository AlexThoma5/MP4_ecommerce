from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):

    def test_form_is_valid_with_all_fields_filled(self):
        """Form should be valid when optional fields are filled"""
        form = UserProfileForm({
            'default_full_name': 'Alex Test',
            'default_phone_number': '07123456789',
        })
        self.assertTrue(
            form.is_valid(),
            msg='Form is not valid with all optional fields filled')

    def test_form_is_valid_with_no_fields_filled(self):
        """Form should be valid even when optional fields are empty"""
        form = UserProfileForm({
            'default_full_name': '',
            'default_phone_number': '',
        })
        self.assertTrue(
            form.is_valid(),
            msg='Form is not valid when optional fields are empty')
