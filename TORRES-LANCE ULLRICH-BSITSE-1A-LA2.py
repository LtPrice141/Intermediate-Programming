print('---Comparison Operators---')
while True:
    try:
        x = int(input('Enter number for x: '))
        y = int(input('Enter number for y: '))
        print(f'\n(x={x}, y={y}): x > y = {x>y}')
        print(f'(x={x}, y={y}): x >= y = {x>=y}')
        print(f'(x={x}, y={y}): x < y = {x<y}')
        print(f'(x={x}, y={y}): x <= y = {x<=y}')
        print(f'(x={x}, y={y}): x == y = {x==y}')
        print(f'(x={x}, y={y}): x != y = {x!=y}')
        break
    except ValueError:
        print('Please enter a valid number!')