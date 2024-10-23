from datetime import*
cdt = datetime.now()
biriyani=150
parota=20
rice=20
print("      biryani mane ")
print("   address - laggere")
print(" menu")
print(" (01) biriyani -- 150 rs ")
print(" (02) parota -- 20 rs")
print("(03)rice -- 30 rs")
print("what u like to order")
opt=int(input("enter the opt of the food"))
if( opt == 1):
    print("how many biriyani you want")
    qnt=int(input("enter the number of biriyani u want"))
    print("your order is biriyani")
    print(qnt)
    print(" your total is ", biriyani * qnt)
    print("would u like some more")
    opt2=int(input("enter the option"))
    if (opt2 == 2):
        print (" how many parota you want")
        qnt1= int(input("enter the number of parota u wnat"))
        print(" parota is ",parota*qnt1)
print(" ******your total bill is *****")
print("      biryani mane " "  " , cdt)
print("   address - laggere" )
b1=biriyani*qnt
b2=parota*qnt1
b3= b1+b2

print ( " opt  item    qnt  price ")
print (opt , "   biriyani "  , qnt , biriyani*qnt)
print (opt2 , "  parota   "  , qnt , parota*qnt1)
print ( "-----------------------------")
print("your total billl is ",b3)









    
    