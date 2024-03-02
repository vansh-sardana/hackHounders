# falls/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import PasswordInput
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')


from .models import EmergencyContact

class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ['name', 'phone', 'email']
def clean_phone(self):
        phone = self.cleaned_data['phone']
        # Check if a contact with the same phone number already exists
        if EmergencyContact.objects.filter(phone=phone).exists():
            raise ValidationError("Contact with the same phone number already exists.")
        return phone


from .models import CustomUser  # Import your custom user model

class CustomUserCreationForm(UserCreationForm):
    custom_field1 = forms.CharField(max_length=255, required=True)
    custom_field2 = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('custom_field1', 'custom_field2')


class UserLoginForm(AuthenticationForm):
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=PasswordInput(render_value=False),  # Set render_value to False
    )

    class Meta:
        model = User
        fields = ('username', 'password')
