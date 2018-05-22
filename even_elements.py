import os


play = True

print("This will return a list of even numbers")

while play == True:

	print("Enter a list of numbers:")
	print("Example: 1,5,7,8,9,10,30")

	input_list = input("--> ")
	input_list = input_list.replace("' ","")
	split_list = input_list.split(",")
	even_el_list = []


	even_el_list = split_list[::2]


	print(even_el_list)

	play_again = input('Do you want to play again? "Yes" or "No": ')

	if play_again == "yes":
		play = True
		os.system('clear')
	else:

		play = False

