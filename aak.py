print("................WELCOME TO AVINASH BANK...............")
a=200000
pin="1234"
x=input("Enter Your Pin")

if(x==pin):
    print("successfully login, Now choose an option")
    print("1.withdrawl")
    print("2.balance enquiry")
    print("3.change pin")
    print("4.deposit")
    y=int(input("enter your choice"))
    if(y==1):
        d=int(input("Enter Amount To be withdrawl "))
        print("withdrawlucessful of amount")
        sum=a+d
        print("Now your Total balance is ",sum)
    elif(y==2):
        w=int(input("the pin change"))
        if(w%100==0):
            print(w,"is Withdraw From your a/c")
            sub=a-w
            print("Now Your Clear balance is",sub)
        else:
            print("This amount canot be withdrawing ")
    elif(y==3):
        print("your amount balance is ",a)
    elif(y==4):
        p=input("Enter Your Pin")
        if(p==pin):
            q=int(input("deposit"))
            n=q
            print("Your Password  Changed Successfully ")
            print("\tyour new pin is ",n)
        else:
            print("You choose an wrong Number "/n)
    else:
        l=input("your Pin is incorrect  Enter again"/n)
    """for (l!=n,m==0,m<4,m++):
        print("you have mor Three chances Try again" /n"after this your accont has been temporarily blocked ") 
        break"""
    
