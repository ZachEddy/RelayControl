from django import forms
import RPi.GPIO as GPIO


class RelayForm(forms.Form):
	CHOICES = (('on', 'on',), ('off', 'off',))

	relay_one = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES)
	relay_two = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES)
	relay_three = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES)
	relay_four = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES)
