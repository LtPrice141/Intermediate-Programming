print('\n---System Login---')

#username = input('Set username: ')
#password = input('Set password: ')

username = "lance"
password = "pogi"

check_user = input('Input username: ')
check_passw = input('Input password: ')

if check_user == username:
    if check_passw == password:
        print('Welcome! Login successful.')
    
    else:
        print('Incorrect password.')

else:
    print('User not found.')