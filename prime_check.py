def prime (N) :
    count = 0 

    for i in range(2,N) :
        if N % i == 0 :
            count += 1 
    if  count == 0 :
        print("True")
    else :
        print("False")

N = int(input("Enter the Number :- "))
prime(N)