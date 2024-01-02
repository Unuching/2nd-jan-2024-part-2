import random 

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

number_of_letters = int(input("How many letters do you want?"))

no_of_numbers = int(input("How many numbers do you want?"))

number_of_symbols = int(input("How many symbols do you want?"))

selected_letters = random.sample(letters, number_of_letters)

selected_numbers = random.sample(numbers, no_of_numbers)

selected_symbols = random.sample(symbols, number_of_symbols)

password_list = selected_letters+selected_numbers+selected_symbols

random.shuffle(password_list)

password = "".join(password_list)

print(password)