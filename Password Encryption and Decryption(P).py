import string


l=string.digits+string.ascii_lowercase+string.ascii_uppercase+string.punctuation
num=len(l)


def encrypt(p,key):
    c=''
    for i in p:
        if not i==' ':
            index=l.find(i)
            n=index+key
            if n>=num:
                n-=num
            c+=l[n]
    print(c)

def decrypt(c,key):
    p=''
    for i in c:
        if not i==' ':
            index=l.find(i)
            n=index-key
            if n<0:
                n+=num
            p+=l[n]
    print(p)


def Menu():
    while True:
        print("1)Encryption\n2)Decryption\n3)Exit")
        x=int(input("Enter Choice: "))
        if x==1:
            print("Encryption")
            password=input("Enter Password to encrypt: ")
            key=int(input("Enter shift key: "))
            encrypt(password,key)
        elif x==2:
            print("Decryption")
            password=input("Enter Password to decrypt: ")
            key=int(input("Enter shift key: "))
            decrypt(password,key)
        elif x==3:
            print("Bye Bye")
            break
        else:
            break

Menu()