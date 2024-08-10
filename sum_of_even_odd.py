def sum_of_even_odd(l) :
    sum_even = 0 
    sum_odd = 0
    for i in l :
        if i % 2 == 0 :
            sum_even += i 
        else :
            sum_odd += i 
    t = (sum_even,sum_odd)
    return t 

L = [1,2,3,4,5,6] 
print(sum_of_even_odd(L))