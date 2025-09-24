food=["burger","pizza","fries","aloo wrap","chicken nuggets","tea","coffee","coke","brownie","choco lava"]
prices=[100,200,60,50,150,25,70,40,120,90]

myorderfood=[]
myordercost=[]

print("welcome to McDoonald's take away")

for i in zip(food,prices):
    print(i)
    
order=input("can i take your order?(yes/no):")
if order=="no":
    print("thankyou,have a great day!")
    exit()

nextorder=True
while nextorder==True:

 foodorder=input("please enter the item (1 item at a time):")

 if foodorder=="burger":
     myorderfood.append(food[0])
     myordercost.append(prices[0])
 elif foodorder=="pizza":
     myorderfood.append(food[1])
     myordercost.append(prices[1])
 elif foodorder=="fries":
     myorderfood.append(food[2])
     myordercost.append(prices[2])
 elif foodorder=="aloo wrap":
     myorderfood.append(food[3])
     myordercost.append(prices[3])
 elif foodorder=="chicken nuggets":
     myorderfood.append(food[4])
     myordercost.append(prices[4])
 elif foodorder=="tea":
     myorderfood.append(food[5])
     myordercost.append(prices[5])
 elif foodorder=="coffee":
     myorderfood.append(food[6])
     myordercost.append(prices[6])
 elif foodorder=="coke":
     myorderfood.append(food[7])
     myordercost.append(prices[7])
 elif foodorder=="brownie":
     myorderfood.append(food[8])
     myordercost.append(prices[8])
 elif foodorder=="choco lava":
     myorderfood.append(food[9])
     myordercost.append(prices[9])
 else:
     print("not on menu")
 finished=input("have you finished ordering?")
 if finished=="no":
     nextorder=True
 else:
     nextorder=False

 if finished=="yes":
    print("here is your order!")
    print("***visit again***")
 print("the order is",myorderfood)
 print("the price is",myordercost)

 
import mysql.connector as c
con=c.connect(host='localhost',user='root',passwd='Yashika@05',database='mcd')
cursor=con.cursor()
name=input("enter your name:")
items=int(input("enter the no. of items:"))
num=int(input("enter your reviews(_/5):"))
query="insert into mcd1 values('{}',{},{})".format(name,items,num)
cursor.execute(query)
con.commit()
print("thankyouu for the information")
 
          

    

