from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, UserProfile


class CustomUserCreationForm(UserCreationForm):
    """
    This code is taken from the following tutorial:
    https://testdriven.io/blog/django-custom-user-model/
    """

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("email", "first_name", "last_name")

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "email": "Email",
            "first_name": "First Name",
            "last_name": "Last Name",
            "password1": "Password",
            "password2": "Repeat Password",
            "is_staff": "Is Staff?",
            "is_superuser": "Is Superuser",
            "is_active": "Active?"
        }
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder


class CustomUserChangeForm(UserChangeForm):
    """
    This code is taken from the following tutorial:
    https://testdriven.io/blog/django-custom-user-model/
    """

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes for user profile form.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_phone_number": "Phone Number",
            "default_postcode": "Postal Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County, State or Locality",
        }

        self.fields["default_phone_number"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "default_country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = (
                "rounded-0 " "profile-form-input"
            )
            self.fields[field].label = False
