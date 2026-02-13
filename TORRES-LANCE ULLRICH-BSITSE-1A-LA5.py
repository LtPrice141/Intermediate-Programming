print('\n---Grade Calculator Program---')

grade = int(input('What is your score?: '))

if grade < 0 or grade > 100:
    print('Invalid score!')

elif grade >= 95:
    print('Grade: A+ — Very good!')

elif grade >= 90:
    print('Grade: A- — Excellent work!')

elif grade >= 85:
    print('Grade: B+ — Great job!')

elif grade >= 80:
    print('Grade: B- — Good work!')

elif grade >= 75:
    print('Grade: C+ — Nice effort!')

elif grade >= 70:
    print('Grade: C- — You passed!')

elif grade >= 60:
    print('Grade: D — Needs improvement.')

else:
    print('Grade: F Better luck next time.')