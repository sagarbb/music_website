from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms.models import ModelForm

from django.forms.widgets import FileInput

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
