from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from VoizApp.models import buy, recharging, issue, invoice, prepaid, postpaid, dongle


class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']


class kycform(forms.ModelForm):

  class Meta:
    model= buy
    fields= "__all__"


class rechargeform(forms.ModelForm):

  class Meta:
    model = recharging
    fields = "__all__"


class issueform(forms.ModelForm):
  class Meta:
    model= issue
    fields="__all__"


class invoiceform(forms.ModelForm):
  class Meta:
    model = invoice
    fields ="__all__"

class prepaidform(forms.ModelForm):
  class Meta:
    model = prepaid
    fields ="__all__"


class postpaidform(forms.ModelForm):
  class Meta:
    model = postpaid
    fields ="__all__"

class dongleform(forms.ModelForm):
  class Meta:
    model = dongle
    fields ="__all__"



