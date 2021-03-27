number = int(input("enter a number"))
 
#first to number
n1 , n2 = 0 , 1
#universal value
count = 0

if number <= 0:
    print("please enter positive number")
elif number == 1:
    print("fabonacci series upto",number,":")
    print(n1)
else:
    print("fabonacci series")
    while count < number:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2=nth
        count+= 1







