print("Give public keys of User 1 & User 2") 
S=int(input("public key of User 1 ")) 
G=int(input("public key of User 2 ")) 
PR1=int(input("Select private key of User 1 ")) 
PR2=int(input("Select private key of User 2 ")) 
x= G**PR1%S
y= G**PR2%S
print("User 1 & User 2 exchanges their Public Keys") 
K1=y**PR1%S
K2=x**PR2%S
print(K1 ,K2 ,"symmetric keys For Both users")
print("Secret Message is " ,K1)
