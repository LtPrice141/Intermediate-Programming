print('---Convert Years to Seconds---')
while True:
    try:
        years = int(input('Enter number of years: '))
        converted = (years * 31536000)
        print(f'{years} year/s to seconds is {converted:,} seconds')
        print('Thank you for using this program.')
        break
    
    except ValueError:
        print('Please input a valid number.')