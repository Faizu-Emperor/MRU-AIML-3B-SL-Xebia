def largest(l) :
    greater = l[0]
    for i in l :
        if i > greater :
            greater = i 
    return greater

L = [1,2,3,4,5,6,7,8,9,10]
print("Largest number is :-",largest(L))
