import random
 
passlen=int(input("Enter the length of password:"))

s="abcdefghijklmnopqrstuvwxyz0123456780ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

p="".join(random.sample(s,passlen))
print (p)