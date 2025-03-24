from data import letters, numbers, special_char
from main_class import BrainPassGenerator

all_types_list = [letters, numbers, special_char]

password_generator = BrainPassGenerator(all_types_list)

print('*********************')
print('* PASSWORD GENERATOR *')
print('*********************')

print('Welcome in password generator, fill in all inputs, minimum value is 0.\n')

lets_continue = 'Yes'

while lets_continue == 'Yes':

    leters_type = int(input('Set number of letters in your password: '))
    numbers_type = int(input('Set number of numbers in your password: '))
    special_char_type = int(input('Set number of special chars in your password: '))
   
    result = password_generator.counter_type(leters_type, numbers_type, special_char_type)

    print(f'Your password is: {result}')
    lets_continue = input('Do you want to generate another password ? For continue, write "Yes" or "No": ')
    if lets_continue != 'Yes':
        print('Thank you for using this app.') 





