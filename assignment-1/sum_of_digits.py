def sum_digits(N) :
    sum = 0

    for i in N :
        sum += int(i) 
    print(sum)

N = input("Enter the Number :- ")
sum_digits(N)