A = input("Enter a number: ")
if A.isdigit():
    A = int(A)
    if A%2==0:
        print("EVEN")
    else:
        print("ODD")

elif A.isalpha()or A=="":
    print("Bad input.")

