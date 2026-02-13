print('\n---Eligibility Checker---')

age = int(input('Please enter your age: '))
val_id = input('Do you have a valid ID? (yes/no): ').strip().lower()

# Valid ID checking
if val_id == "yes" or val_id == "y":
    val_id = True

elif val_id == "no" or val_id == "n":
    val_id = False

else:
    print('Invalid input. Yes or no only!')
    val_id = None

# Eligibility checking
if age >= 60 and val_id == True:
    print('Eligible for senior discount!')

elif age >= 18 and val_id == True:
    print('Eligible!')

else:
    print('Not eligible!')