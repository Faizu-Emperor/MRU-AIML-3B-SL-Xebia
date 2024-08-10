def v_c_count(w) :
    v = ['a','e','i','o','u']
    count_vowels = 0 
    count_consonants = 0 

    for i in w :
        if i.lower() in v :
            count_vowels += 1 
        elif i == " " :
            continue
        else :
            count_consonants += 1
    return count_vowels,count_consonants

W = input("Enter the Word :- ")
v,c = v_c_count(W)
print("Vowles :-",v,"Consonants :-",c)