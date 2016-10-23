number_t = input("Enter number of triangle numbers:")
number = int(number_t)
for i in range(1, number+1):
    outcome = (i*(i+1))/2
    print(outcome, end=',')
