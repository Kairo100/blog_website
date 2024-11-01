# to make registration form in django to the html page so that user can be register 
#making form.py and all of this that written inside it

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('email', 'username', 'password1', 'password2')