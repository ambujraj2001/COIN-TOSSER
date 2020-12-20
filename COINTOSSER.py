#coin tosser
import random
print("Welocme to coin tosser")
print("Enter TOSS to toss the coin ")
s=input()
if s=="toss" or s=="TOSS" :
   l=["HEADS","TAILS"]
   t=random.randint(0,9)
   if t%2==0 :
       print(l[0])
   else:
       print(l[1])
else:
   print("wrong input try again")

