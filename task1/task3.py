
'''

Write a program that sells "Mars" and "Snickers" bars.
The prices of the bars are like 3 and 4 euros.
The selling machine is to be able to give its user the remainder
in 5, 2, and 1 zloty coins.

For instance, a user indicates that she wants a "Mars" bar
and puts 20 zlotych into the machine. The machine is
to return 17 zlotych with 3 coins of 5 zlotych and 1 coin
worth 2 zlote. These value should be printed out.

'''

machine_is_working = True
mars_cost = 3
snickers_cost = 4

five_zl_value = 5
two_zl_value = 2

# while machine_is_working:
given_money_zl = int(input('Enter the amount of money the user gives: '))
bar_title = input('Enter the title of a bar (Snickers, Mars): ')
remainder = 0

if bar_title == 'Snickers':
    remainder = given_money_zl - snickers_cost

if bar_title == 'Mars':
    remainder = given_money_zl - mars_cost

print('change to be given out: ', remainder)

n_five_zl_coins = (remainder - remainder % five_zl_value) / five_zl_value

remainder = remainder - n_five_zl_coins * five_zl_value

print('5 zl: ', n_five_zl_coins)

# print('remainder is ', remainder)

if remainder == 0:
    n_two_zl_coins = 0
else:
    n_two_zl_coins = (remainder - remainder % two_zl_value) / two_zl_value

remainder = remainder - n_two_zl_coins * two_zl_value

print('2 zl: ', n_two_zl_coins)

if not remainder == 0:
    print('1 zl: ', remainder)

    # Mars -- 3 euros
    # Snickers -- 4 euros
    # Machine can give its user the remainder in 5, 2, and 1 zloty coins

