print("Enter an integer in decimal form")
dec = int(input())
print("Enter 1/2/3: 1.Binary , 2.Octal , 3.Hexadecimal")
choice=input()
inte = dec
rem = ""
while(inte>0):
    if choice=='1':
        quo = inte//2
        rem+= str(inte%2)
        inte = inte//2
    elif choice=='2':
        quo=inte//8
        rem+=str(inte%8)
        inte=inte//8
    else:
        quo=inte//16
        rem+=str(inte%16)
        inte=inte//16
print(rem[::-1])
