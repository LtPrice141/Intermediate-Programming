print('\n=== MOVIE TICKET SYSTEM ===')

day = input('Day (weekday/weekend): ').lower().strip()
customer_type = input('Type (regular/student/senior): ').lower().strip()
time = int(input('Showtime hour (9-22): '))
ticket_qty = int(input('Number of tickets: '))
user_disc = 0
matinee_disc = 0
group_disc = 0

if day == "weekday":
    base_p = 200
else:
    base_p = 300

ticket_qty_calc = base_p * ticket_qty

if customer_type == 'student':
    user_disc = ticket_qty_calc * 0.20 # 20% off

elif customer_type == 'senior':
    user_disc = ticket_qty_calc * 0.30 # 30% off

if time >= 9 and time <= 22:
    if time <12:
        matinee_disc = ticket_qty_calc * 0.10 # 10% off

else:
    print('Invalid time selected. (9-22 only)')


if ticket_qty > 0:
    if ticket_qty >=5:
        group_disc = ticket_qty_calc * 0.05 #5% off
else:
    print('A minimum of 1 ticket is required.')


print('\n--- Receipt ---')
print(f'Base Price: {base_p} x {ticket_qty} = {ticket_qty_calc:,.2f}')

if customer_type == 'student':
    print(f'Student Discount (20%): -{user_disc:,.2f}')

elif customer_type == 'senior':
    print(f'Senior Discount (30%): -{user_disc:,.2f}')

if time >=9 and time <= 22:
    if time < 12:
        print(f'Matinee Discount (10%): -{matinee_disc:,.2f}')

if ticket_qty >= 5:
    print(f'Group Discount (5%): -{group_disc:,.2f}')

final_total = ticket_qty_calc - user_disc - matinee_disc - group_disc

print(f'TOTAL: {final_total:,.2f}')
print('Thank you for your purchase!')