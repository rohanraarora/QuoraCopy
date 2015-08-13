from django import forms
from .models import QuoraUser
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
	username = forms.CharField(label = "Username")
	password = forms.CharField(label = "password",widget=forms.PasswordInput)

	def __init__(self,*args,**kwargs):
		self.user_cache = None
		super(LoginForm,self).__init__(*args,**kwargs)

	def clean(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and Password:
			self.user_cache = authenticate(username = username,password=password)
			if self.user_cache is None:
				raise forms.ValidationError("Please enter correct Username and Password")
			elif not self.user_cache.is_active:
				raise forms.ValidationError("Inactive User")
		return self.cleaned_data

	def get_user(self):
		return self.user_cache

class SignUpForm(forms.ModelForm):
	password_text = forms.CharField(label="Password",widget=forms.PasswordInput)
	confirm_password = forms.CharField(label="Confirm Password",widget = forms.PasswordInput,help_text = "Confirm your password")
	def __init__(self,*args,**kwargs):
		super(SignUpForm,self).__init__(*args,**kwargs)
		self.fields['email'].required = True
		self.fields['username'].requied = True
		self.fields['first_name'].required= True
		self.fields['last_name'].required = True
	def clean_confirm_password(self):
		password_text = self.cleaned_data.get("password_text")
		confirm_password = self.cleaned_data.get("confirm_password")
		if password_text and confirm_password and password_text != confirm_password:
			raise forms.ValidationError("Passwords don't match")
		return confirm_password

	def clean_email(self):
		email_data = self.cleaned_data.get("email")
		if email_data and len(QuoraUser.objects.filter(email = email_data)) > 0:
			raise forms.ValidationError("User with this email already exists")
		return email_data

	def clean_username(self):
		username_data = self.cleaned_data.get("username")
		if username_data and len(QuoraUser.objects.filter(username = username_data)) > 0:
			raise forms.ValidationError("Username already exists")
		return username_data

	def save(self,commit = True):
		user = super(SignUpForm,self).save(commit=False)
		user.set_password(self.cleaned_data.get("password_text"))
		if commit:
			user.save()
		return user


	class Meta:
		model = QuoraUser
		fields = ["first_name","last_name","username","email"]
