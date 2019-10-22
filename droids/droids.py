import time
import random
from random import randint

print('\n' * 100)
print('\n\n[-Droids : by jay : type help-]')
print('\n\n\n------------------------')
print('        DROIDS')
print('------------------------')
print('\n10.03.2245 : cytek inc.')
time.sleep(1)
print('\nCTRL866 Re-Boot Sequence....')
time.sleep(1)
print('\nInitalizing Control Droid 866....')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
time.sleep(1)
print('Laser offline...')
time.sleep(1)
print('Motion Tracker offline...')
time.sleep(1)
print('\nService Port avaliable...')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
print('\nControl Droid Active.')
time.sleep(1)
print('''\n\nYou are the 866 Control Droid aboard 
the Droid Shuttle 'KERNEL'. Enemy droids have boarded
and have taken over flight path. You are damaged & have been 
re-initialized but your laser and motion tracker are offline.''')

def start(inventory):
	print('\n----------')
	print('\nDroid mobile..')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('\n[-MAIN ELEVATOR-]')
	print('\n1.) deck 1 - Security')
	print('2.) deck 2 - Maintenance')
	print('3.) deck 3 - Cargo Hold - Airlock')
	print('4.) deck 4 - Droid Hangar')
	print('5.) deck 5 - Shuttle Control')
	print('6.) deck 6 - Observation\n')
	
	cmdlist = ['1', '2', '3', '4', '5', '6',]
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		security(inventory)
	elif cmd == '2':
		if 'droid hack' in inventory:
			print('\n- DECK 2 - MAINTENANCE LOCKED -')
			time.sleep(2)
			start(inventory)
		else:
			maintenance(inventory)
	elif cmd == '3':
		cargo_hold(inventory)
	elif cmd == '4':
		if 'laser' in inventory:
			print('\n- DECK 4 - DROID HANGAR LOCKED -')
			time.sleep(2)
			start(inventory)
		else:
			droid_hangar(inventory)
	elif cmd == '5':
		shuttle_control(inventory)
	elif cmd == '6':
		if 'motion tracker' in inventory:
			print('\n- DECK 6 - OBSERVATION LOCKED -')
			time.sleep(2)
			start(inventory)
		else:
			observation(inventory)
		
def maintenance(inventory):
	print('\n----------')
	print('\nDroid mobile..')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('''\nThis is the maintenance deck and it appears deserted. 
You can see a terminated crew droid, it has sustained
severe laser fire.''')
	print('\n[-MAINTENANCE-]\n')
	print('1.) 716 Crew Droid')
	print('2.) Return to Main Elevator\n')
	
	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)
	if cmd == '1':
		crew_droid(inventory)
	elif cmd == '2':
		start(inventory)
		
def crew_droid(inventory, items=['droid hack']):
	print('\n----------')
	print('''\n716 has a droid hack program and it's connection
outlet is still intact. You can connect to this droid with service
port and download the program.''')
	if len(items) > 0:
		for item in items:
			print('\n--> %s' % (item))
			print('\n\n1.) Exit.')
	cmdlist = ['service port', '1']
	cmd = getcmd(cmdlist)
	if cmd == 'service port':
			inventory.append('droid hack')
			items = ['droid hack']
			print('\nservice port connected.')
			time.sleep(1)
			print('accessing file..')
			time.sleep(1)
			print('downloading..')
			time.sleep(1)
			print('....')
			time.sleep(1)
			print('\ndownload complete.')
			print('\nYou have the droid hack program and return')
			print('to the Main Elevator.')
			time.sleep(2)
			start(inventory)
	elif cmd == '1':
			maintenance(inventory)
	else:
		print('\n error. invalid command-')
	
def cargo_hold(inventory):
	print('\n----------')
	print('\nDroid mobile..')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('''\nYou enter the Cargo Hold, two Enemy Combat droids
unload a barrage of laser fire at you. Their fire is very accurate
and you take a direct hit in your main CPU.''')
	print('\n[-CARGO HOLD - AIRLOCK-]')
	print('....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('\nshutdown imminent...')
	time.sleep(1)
	print('CTRL866 offline.')
	time.sleep(1)
	print('Droid terminated.')
	print('\nGAME OVER\n')
	exit(0)
	
def droid_hangar(inventory):
	print('\n----------')
	print('\nDroid mobile..')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('''\nThe Droid Hangar is filled with debri. There
is laser scoring everywhere and all droids are terminated.
In the corner there is one inactive repair droid still in his security
cylinder. You can initialise the droid to repair your laser but you will 
require a 3 digit access code.\n''')
	print('[-DROID HANGAR-]')
	print('\n1.) Repair Droid 3 digit code')
	print('2.) Return to Main Elevator')
	
	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		access_code(inventory)
	elif cmd == '2':
		start(inventory)
		
def access_code(inventory):
	code = '%d%d%d' % (randint(0,9), randint(0,9), randint(0,9))
	guess = input('\n[KEYPAD]> ')
	guesses = 0
	
	while guess != code and guess != 'yu8xxj3' and guesses <4:
		print('\n* ACCESS - DENIED *')
		guesses += 1
		guess = input('\n[KEYPAD]> ')
		
	if guess == code or guess == 'yu8xxj3':
		repair_droid(inventory)
	else:
		print('\n....')
		time.sleep(1)
		print('\n....')
		time.sleep(1)
		print('\nKEYPAD - LOCKED')
		time.sleep(1)
		print('\ncode randomizing..')
		time.sleep(1)
		print('\nKEYPAD - OPEN')
		time.sleep(1)
		droid_hangar(inventory)
		
def repair_droid(inventory, items=['laser']):
	print('\n\n----------')
	print('\nREP323 boot sequence....')
	time.sleep(1)
	print('Initalizing Repair Droid 323....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('Repair Droid Active.')
	time.sleep(1)
	print('''\nThe Repair droid is now active. You MUST connect to
this droid with service port to repair laser.''')

	if len(items) > 0:
		for item in items:
			print('\n--> %s' % (item))
	cmdlist = ['service port']
	cmd = getcmd(cmdlist)
	if cmd == 'service port':
			inventory.append('laser')
			items = ['laser']
			print('\nservice port connected.')
			time.sleep(1)
			print('Repairing Laser...')
			time.sleep(1)
			print('Auto alignment...')
			time.sleep(1)
			print('....')
			time.sleep(1)
			print('\nLASER ONLINE.')
			print('''\nYour laser is now online. You de-activate the Repair
Droid and return to the Main Elevator.''')
			time.sleep(2)
			start(inventory)
	else:
		print('\n error. invalid command-')
		
def security(inventory):
	print('\n----------')
	print('\nDroid mobile..')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('''\nYou are on the Security Deck. This is where all
surveillance aboard the shuttle is done. Sentry droid 343 has been
terminated. You MUST access the Sentry droid's logs but you
will have to hack the data recorder.\n''') 
	print('[-SECURITY-]\n')
	print('1.) View Surveillance monitors on other decks')
	print('2.) Hack Sentry droid 343')
	print('3.) Return to main elevator')
	
	cmdlist =['1', '2', '3']
	cmd = getcmd(cmdlist)
	
	if cmd == '1':
		print('\n----------')
		print('\nBooting Monitors....')
		time.sleep(1)
		print('....')
		time.sleep(1)
		print('...')
		time.sleep(1)
		print('Monitors active.')
		time.sleep(1)
		print('\n[-SURVEILLANCE FEED-]')
		print('''\n-The Hangar monitor is offline you have no live feed.
\n-In the Cargo hold there are two Enemy Combat droids patroling.
\n-The Maintenance deck looks clear except for a few terminated droids.
\n-An Elite Enemy Command droid is posted on the Shuttle Control deck.
\n-Observation shows a Enemy Sentry droid.''')
		time.sleep(2)
		security(inventory)
		
	elif cmd == '2':
		if 'droid hack' in inventory:
			print('\nloading droid hack....')
			time.sleep(2)
			print('....')
			time.sleep(2)
			print('10000101010101010101010' * 1000)
