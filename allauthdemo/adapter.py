from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError
from .settings import ACCOUNT_USERNAME_MAX_LENGTH as usermaxlen
from .settings import ACCOUNT_PASSWORD_MAX_LENGTH as passmaxlen


class CustomProcessAdapter(DefaultAccountAdapter):

	'''
		Google login fails without "shallow" parameter in clean_username,
		may affect other uses too.
		
		Suggest to use "shallow=False", which will help avoid duplicate account names. ie:
		
		clean_username(self, username, shallow=False)
	'''
	
	def clean_username(self, username, shallow=False):
		if len(username) > usermaxlen :
			raise ValidationError('Please enter a username of ' + str(usermaxlen) + ' characters or less.')
		return DefaultAccountAdapter.clean_username(self,username) # For other default validations.

	def clean_email(self,email):
		RestrictedList = ['test@test.com']
		if email in RestrictedList:
			raise ValidationError('You are restricted from registering. Please contact admin.')
		return email

	def clean_password(self,password, user=None):
		if len(password) > passmaxlen :
			raise ValidationError('Please enter a password of ' + str(passmaxlen) + ' characters or less.')
		return DefaultAccountAdapter.clean_password(self,password)