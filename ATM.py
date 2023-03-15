while True:
    balance=10000
    
    print("ATM")
    print("""
          
          1)   Balance
          2)   Withdraw
          3)   Deposite
          4)   Quit
          
          """)
    try:
        option=int(input("Enter option: "))
        
    except:
        #print("Error",e)
        print("Enter 1,2,3 or 4 only")
        
    if option==1 :
        print("Your Account Balance is: ",balance)
        
    if option==2:
        print("Your Account Balance is: ",balance)
        withdraw=float(input("Enter amount: "))
        
        if withdraw>balance:
            print("No funs in account")
        
        if withdraw>0 and withdraw<balance:
            total=(balance-withdraw)
            print("Remaining amount in your account is: ",total)
        
        
        
         
        else:
            print("none withdraw made")
            
    if option==3:
        print("Your Account Balance is: ",balance)
        
        Deposit=float(input("Enter amount to deposit: "))
        
        if Deposit>0:
            total1=(balance+Deposit)
            
            print("Total amount is : ",total1)
            
        else:
            print("None Deposit mode")
            
    if option==4:
        exit()
        