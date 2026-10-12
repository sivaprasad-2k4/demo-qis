balance=5000
while True:
    print("........ATM CONSOLE APPLICATION.........")
    print("1.check balance")
    print("2.deposit money")
    print("3.withdraw money")
    print("4.exit")

    choose=input("enter your choice(1-4):")
    if choose == '1':
        print("your current balance is :",balance)
    elif choose =='2':
        deposit=int(input("enter amt to be deposited:"))
        if deposit>0:
            balance=balance+deposit
            print("amount deposited successfully")
            print("updated balance is",balance)
        else:
            print("enter a valid amount")
    elif choose=='3':
        withdraw=int(input("enter amount to be withdrawn:"))
        if withdraw>0:
            if withdraw<=balance:
                balance=balance-withdraw
                print("successfully withdrawed",withdraw,"rupees")
                print("remaining balance is:",balance)
            else:
                print("transaction rejected")
                print("insufficient balance")
    elif choose=='4':
        break
