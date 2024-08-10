def multiples_of_number(n,l) :
    for i in range(n,l + 1) :
        if i % n == 0 :
            print(i,end = " ") 

N = int(input("Enter the Number :- "))
L = int(input("Enter Limit :- "))
multiples_of_number(N,L)