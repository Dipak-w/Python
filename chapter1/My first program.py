#Taking input from user and printing it
name = input("name:")
age = int(input("age: "))
price = float(input("price: "))

print("My name is", name, "and I am", age, "years old", "my House price is", price )


#Conditional program

A = int(input("A : "))
G = input("M/F : ")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 1000")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 2000")
elif(A == 5 or G =="M"):
    print("fee is 500")
else:
    print("No fee")