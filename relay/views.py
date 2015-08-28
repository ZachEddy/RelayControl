from django.http import HttpResponse
from django.shortcuts import render, redirect
import RPi.GPIO as GPIO
from . import forms

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.output(8, 1)
GPIO.output(12,0)
GPIO.output(16,1)

GPIO.setup(18, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(26, GPIO.IN)

def index_view(request):
	if request.method == 'POST':
		form = forms.RelayForm(request.POST)
		if(form.is_valid()):
			relay_one = form.cleaned_data['relay_one']
			relay_two = form.cleaned_data['relay_two']
			relay_three = form.cleaned_data['relay_three']
			relay_four = form.cleaned_data['relay_four']
			print relay_one
			if relay_one == 'on':
				GPIO.output(8,0)
				print "ON"
			else:
				GPIO.output(8,1)
				print "OFF"
			if relay_two == 'on':
                                GPIO.output(10,0)
                        else:
                                GPIO.output(10,1)
			if relay_three == 'on':
                                GPIO.output(12,0)
                        else:
                                GPIO.output(12,1)
			if relay_four == 'on':
                                GPIO.output(16,0)
                        else:
                                GPIO.output(16,1)
			return redirect('/relay/')
	else:
		initial_state = determine_initial()
		form = forms.RelayForm(initial = initial_state)
	return render(request, "relay.html", {'form':form})


def determine_initial():
	initial_dict = {}
	print GPIO.input(18)
	if (GPIO.input(18)):
		initial_dict['relay_one'] = 'on'
	else:
		initial_dict['relay_one'] = 'off'
	
	if (GPIO.input(22)):
                initial_dict['relay_two'] = 'on'
        else:
                initial_dict['relay_two'] = 'off'

	if (GPIO.input(24)):
                initial_dict['relay_three'] = 'on'
        else:
                initial_dict['relay_three'] = 'off'
	
	if (GPIO.input(26)):
                initial_dict['relay_four'] = 'on'
        else:
                initial_dict['relay_four'] = 'off'
	
	return initial_dict
















