from django.test import TestCase
from taxi.forms import DriverCreationForm


class TestForms(TestCase):
    def test_author_creation_form_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "Testuser123!",
            "password2": "Testuser123!",
            "first_name": "Test first",
            "last_name": "Test last",
            "license_number": "ADM56984",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
