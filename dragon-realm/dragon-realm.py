import random
import time
print('\n\n[--system--] one file is bad the other is good ..guess the right one.\n')
print('\n\nconnecting....')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
time.sleep(1)
print('\nconnection established')

def displayIntro():
	print('------------')
	print('SYSTEM FILES')
	print('------------\n')
	print('1.) file.')
	print('2.) file.\n')
	
def chooseOption():
	option = ''
	while option != '1' and option != '2':
		print('which file to download? 1 or 2')
		option = input('user:> ')
		
	return option
	
def checkOption(chosenOption):
	print('\nintialising download....')
	time.sleep(1)
	print('accessing file....')
	time.sleep(1)
	print('downloading....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	
	goodfile = random.randint(1, 2)
	
	if chosenOption == str(goodfile):
		print('\ndownload complete.')
		print('\nGAME OVER')
	else:
		print('\nfile corrupt')
		print('system infected.')
		print('\nGAME OVER')
		
		
playAgain = 'yes'
while playAgain == 'yes':
	displayIntro()
	optionNumber = chooseOption()
	checkOption(optionNumber)
	
	print('\ndownload again? .... (yes or no)')
	playAgain = input('user:> ')