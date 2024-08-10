def reverse(W) :
    reverse_string = ""
    for i in W :
        reverse_string = i + reverse_string
    print(reverse_string)

W = input("Enter the Word :- ")
reverse(W)