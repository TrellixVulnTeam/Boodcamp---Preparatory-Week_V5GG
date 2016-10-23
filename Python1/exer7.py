number_t = input("Enter number of pronic numbers:")
number = int(number_t)
for i in range (1, number+1):
    outcome = i*(i+1)
    print(outcome, end=',')
