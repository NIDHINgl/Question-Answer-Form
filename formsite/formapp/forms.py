from django import forms
from django.core import validators
from .models import loginfiles
from .models import questionfiles
from .models import answerfiles


class loginform(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'email','placeholder':'Enter your Emailid'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password','placeholder':'Enter your Password'}))

class signupform(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'id':'name','placeholder':'Enter your name','autofocus':''}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'email','placeholder':'Enter your Emailid'}))
	phone = forms.CharField(widget=forms.NumberInput(attrs={'id':'phone','placeholder':'Enter your phone No.'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password','placeholder':'Enter your Password'}))

class questionform(forms.Form):
	question = forms.CharField(widget=forms.Textarea(attrs={'id':'question','placeholder':'enter your question','autofocus':''}))

class answerform(forms.Form):
	answer = forms.CharField(widget=forms.Textarea(attrs={'id':'answer','placeholder':'answer here','autofocus':''}))
	idform_id = forms.CharField(widget=forms.NumberInput(attrs={'id':'idform','placeholder':'Enter your question-id'}))
	class meta:
		models=answerfiles
		fields=("idform",)