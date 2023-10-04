

def palindrom():
    while True:
        x = input("Enter a value string/integer: ")
        if x == x[::-1]:
            print("It is a palindrome.")
        else:
            print("It is not a palindrome.")
    return

print(palindrom())



