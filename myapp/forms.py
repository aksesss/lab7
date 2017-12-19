from django import forms
from myapp.models import Goods
from django.contrib.auth.forms import UserCreationForm

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        exclude = []



# class qq(UserCreationForm):
#     """
#     A form that creates a user, with no privileges, from the given username and
#     password.
#     """
#     error_messages = {
#         'password_mismatch': _("The two password fields didn't match."),
#     }
#
#     password2 = forms.CharField(
#         label=_("Password confirmation"),
#         widget=forms.PasswordInput,
#         strip=False,
#         help_text=_("Enter the same password as before, for verification."),
#     )
#
