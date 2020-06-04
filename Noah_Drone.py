# Alysha Noah
# Date: 5/13/2020
# Program Name: Noah_Drone
# Purpose: Simulation using button, drone movement in x, y, z location

# Constants for menu options
UP = 1
DOWN = 2
FORWARD = 3
BACKWARD = 4
LEFT = 5
RIGHT = 6
POSITION = 7
EXIT = 8

# Main function
def main():
	# Create choice variable to control menu
	choice = 0

	x = 0
	y = 0
	z = 0
	orientation = 'north'

	while choice != EXIT:
		# Show menu
		showMenu()

		# Prompt user for choice
		choice = int(input())

		if choice == UP:
			y = y + 1
			orientation = 'north'
			print('You moved up')
		elif choice == DOWN:
			y = y - 1
			orientation = 'south'
			print('You moved down')
		elif choice == FORWARD:
			z = z + 1
			print('You moved forward')
		elif choice == BACKWARD:
			z = z - 1
			print('You moved backward')
		elif choice == LEFT:
			x = x - 1
			orientation = 'west'
			print('You moved left')
		elif choice == RIGHT:
			x = x + 1
			orientation = 'east'
			print('You moved right')
		elif choice == POSITION:
			print('x = ' + str(x) + ' y = ' + str(y) +
			' z = ' + str(z) + ' orientation = ' + orientation)
		elif choice == EXIT:
			print('Thank you for flying the drone!')
		else:
			print('Error: Invalid Selection')

def showMenu():
	print('Which direction would you like to move the drone?')
	print('1 - Move Up')
	print('2 - Move Down')
	print('3 - Move Forward')
	print('4 - Move Backward')
	print('5 - Move Left')
	print('6 - Move Right')
	print('7 - Display Position')
	print('8 - Exit Navigation')

main()