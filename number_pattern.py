def number_pattern(n) :
    for i in range(1,n + 1) :
        print(str(i) * i) 

N = int(input("Enter the Number :-"))
number_pattern(N)