import datetime


print("welcome to atm")
print(" ")
print("enter 1 if u inserted the card")
print("enter 2 if u have not inserted the card ")
card=int(input("enetr the card--"))
balance=2000
accnum=34252343634
cdt=datetime.datetime.now()
if (card ==1):
    print("enter your pin")
elif(card == 2):

    print("insert the card ")
pin=int(input())
userpin=123
if(pin == userpin):
    print("select language")
    print(" (01) ..kannada")
    print("(02)..english")
lan=input("enter the language-->")
if(lan ==1 or 2 ):
    print("select options")
    print("(01) withdraw")
    print("(02).. balance")
    print("(03) .. deposit")
opt=int(input("enetr the options-->"))
if (opt==1):
    print("enetr the amount")
    amt=int(input("enetr the money u need"))
    print("collect your money   $ ",  amt  , "thank you")
    rbalance=balance-amt
    acnum=accnum
    print("your updated value is ",rbalance)
    print("From sbi ")
    print("your acc number", acnum, " branch - laggere",cdt )
    print("your debited amt is ", amt)
    print("your current balance is ",rbalance)
    print("thank you , vist us again")



         
elif (opt==2):
    print("how much you want to deposit")
    print("please place the cash below")
elif(opt==3):
    print("your balance is ____")








