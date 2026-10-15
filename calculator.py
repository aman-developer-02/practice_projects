print("\t---MANUAL CALCULATOR---")
while True:
    choice = int(input('''
1.) Addition
2.)Subtraction
3.)Multiplication
4.)Division
5.)Squaring
6.)Square root
7.)Cube
8.)Cube Root
9.)Exit\n'''))
    if(choice==1 or choice ==2 or choice ==3):
        a = float(input("Enter the First Number :"))
        b = float(input("Enter the Second Number :"))
        if(choice==1):
            sum = a+b
            print("The Sum of the given numbers is:",sum)
        elif(choice==2):
            sub = a-b
            print("The Difference of the given numbers is:",sub)
        elif(choice==3):
            mul = a*b
            print("The Multiplication of the given numbers is:",mul)
    elif(choice==4):
        a = float(input("Enter the Numerator:"))
        b = float(input("Enter the Denominator"))
        if(b!=0):
            div = a/b
            print(f"The Division of {a}/{b} is:",div)
        else:
            print("Division by Zero is not Allowed.")
    elif(choice==5 or choice ==6 or choice == 7 or choice == 8):
        d = float(input("Enter the Number:"))
        if(choice==5):
            sqr = d*d
            print("The Square of the given number is :",sqr)
        elif(choice==6):
            sqrt = d ** 0.5
            print("The Square root of the given number is:",sqrt)
        elif(choice ==7):
            cube = d*d*d
            print("The Cube of the given number is:",cube)
        elif(choice==8):
            crt = d ** (1/3)
            print("The Cuberoot of the given number is:",crt)
    elif(choice==9):
            print("---EXITING THE PROGRAM---")
            break
    else:
        print("---Please Enter a Valid Choice.---")