tab1=[]
tab2=[]
tab3=[]
NP1=input("Enter the customer's 1 full name :")
n1 = int(input("enter the number of items the customer's 1 :"))
t1=0
s1=0
for i in range(0,n1):
    a = float(input(f"Give the price of the item {i+1} :"))
    tab1.append(a)
for i in range(n1): 
    t1=tab1[i]*(1+0.15-0.02)
    s1=s1+t1 
NP2=input("Enter the customer's 2 full name:")
n2 = int(input("enter the number of items the customer's 2:"))
t2=0
s2=0
for j in range(0,n2):
    b = float(input(f"Give the price of the item {i+1} :"))
    tab2.append(b)
for j in range(n2): 
    t2=tab2[i]*(1+0.15-0.02)
    s2=s2+t2 
NP3=input("Enter the customer's 3 full name :")
n3 = int(input("enter the number of items the customer's 3:"))
t3=0
s3=0
for g in range(0,n3):
    c = float(input(f"Give the price of the item {i+1} :"))
    tab3.append(c)
for g in range(n3): 
    t3=tab3[i]*(1+0.15-0.02)
    s3=s3+t3 
print("Facture est : ")    
print("The Total to be paid for the customer",NP1," is :",s1,"DH")
print("The Total to be paid for the customer",NP2," is :",s2,"DH")
print("The Total to be paid for the customer",NP3," is :",s3,"DH")