bal = 50000.00
while(True):
 choice = int(input("Enter your choice :\n" 
 "1. Withdraw\n"
 "2.deposit\n"))
 if(choice==1):
     amount = float(input("Enter Amount to wihtdraw:"))
     if(amount<bal):
         bal-=amount
         print(f"Amount {amount} is debited successfully")
         print("Remaining balance is:",bal)
     elif(amount<=0):
         print("Error! Enter a valid choice")
     else:
         print("insufficent balance")
 elif(choice==2):
     amount = float(input("Enter Amount to deposit(less than 25000):"))
     if(amount<=0.0):
         print("Invalid amount!")
     elif(amount<=25000.00):
         bal+=amount
         print(f"Amount {amount} is deposited successfully")
         print("Current balance:", bal)
     else:
         print("Deposit of amount more than 25000 is not allowed through ATM")
 else:
     print("Please Enter a Valid Choice")
     
