def palin(W) :
    reverse_string = "" 

    for i in W :
        reverse_string = i + reverse_string 
    if reverse_string == W :
        print(W,"is a Palindrome")
    else :
        print(W,"is not a Palindrome")

W = input("Enter the Word :- ")
palin(W)