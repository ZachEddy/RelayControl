from django.http import HttpResponse
from django.shortcuts import render, redirect
import RPi.GPIO as GPIO
from . import forms

# declare pin numbers for relay toggling
relay_one = 8
relay_two = 10
relay_three = 12
relay_four = 16 #pin 14 is ground, so pin 16 instead
relay_dict = {'relay_one':relay_one, 'relay_two':relay_two, 'relay_three':relay_three, 'relay_four':relay_four}

# delcare pin numbers for current relay states (which relays are on?)
relay_one_initial = 18
relay_two_initial = 22
relay_three_initial = 24
relay_four_initial = 26

# tell Pi which board mode to use
GPIO.setmode(GPIO.BOARD)

# these pins control the relays via an Arduino (they're in charge of turning relays on and off)
GPIO.setup(relay_one, GPIO.OUT)
GPIO.setup(relay_two, GPIO.OUT)
GPIO.setup(relay_three, GPIO.OUT)
GPIO.setup(relay_four, GPIO.OUT)

# these pins determine which relays are on, and which are off (again via an Arduino)
GPIO.setup(relay_one_initial, GPIO.IN)
GPIO.setup(relay_two_initial, GPIO.IN)
GPIO.setup(relay_three_initial, GPIO.IN)
GPIO.setup(relay_four_initial, GPIO.IN)

# view to interface with relays
def index_view(request):
	if request.method == 'POST':
		
		# get form data
		form = forms.RelayForm(request.POST)
		if(form.is_valid()):

			# these will either be 'on' or 'off' depending on what the user has specified
			for relay in form.cleaned_data:
				if form.cleaned_data[relay] == 'on':
					GPIO.output(relay_dict[relay],0)
				else:
					GPIO.output(relay_dict[relay],1)


			# relay_one_state = form.cleaned_data['relay_one']
			# relay_two_state = form.cleaned_data['relay_two']
			# relay_three_state = form.cleaned_data['relay_three']
			# relay_four_state = form.cleaned_data['relay_four']

			# 
			# if relay_one_state == 'on':
			# 	GPIO.output(8,0)
			# else:
			# 	GPIO.output(8,1)

			# if relay_two_state == 'on':
			# 	GPIO.output(10,0)
			# else:
   #      GPIO.output(10,1)
				
			# if relay_three_state == 'on':
   #      GPIO.output(12,0)
   #    else:
   #      GPIO.output(12,1)
			# if relay_four_state == 'on':
			# 	GPIO.output(16,0)
   #    else:
   #    	GPIO.output(16,1)
			
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
















