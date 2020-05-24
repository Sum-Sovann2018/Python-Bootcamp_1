A = input("Enter something: ")
if A=="":
    print("[][]")
else:
    print("["+A[0]+"]"+"["+A[len(A)-1]+"]")