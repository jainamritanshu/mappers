from django import forms
import re
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
class RegistrationForm(forms.Form):
	your_name = forms.CharField(label='Name', max_length=100, required=True)
	phone_no = forms.CharField(label='Phone Number', max_length=13, required=True)
	password = forms.CharField(widget=forms.PasswordInput, label='Passsword', max_length=20, required=True)
	password_again = forms.CharField(widget=forms.PasswordInput, label='Confirm Password', max_length=20, required=True)

	def clean_username(self):
		try:
			user = User.objects.get(username__iexact=self.cleaned_data['your_name'])
		except User.DoesNotExist:
			return self.cleaned_data['username']	
		raise forms.ValidationError(_("The username already exists. Please try another one."))
		
	def clean(self):
		if 'password' in self.cleaned_data and 'password_again' in self.cleaned_data:
			if self.cleaned_data['password'] != self.cleaned_data['password_again']:
				raise forms.ValidationError(_("the two passwords do not match, please try again!"))
			return self.cleaned_data		
