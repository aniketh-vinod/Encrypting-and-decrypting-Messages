
sml_sc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while True:
    response = input("Do you want to encrypt(e) or decrypt(d)?>").lower()
    if response=="e" or response=="d":
        break
    else:
        print("Please enter either 'e' or 'd'")
while True:
    key=int(input("Enter any number between 0 and 25 >"))
    if key<0 or key>25:
        print("enter a valid number")
    else:
        break
message=input("Enter your message:").upper()

convert=''
for i in message:
    if i in sml_sc:
        number=sml_sc.find(i)
        if response=='e':
            number=number+key
        elif response=='d':
            number=number-key
        if number>= len(sml_sc):
            number=number-len(sml_sc)
        elif number< 0:
            number=number+len(sml_sc)

        convert+=sml_sc[number]
    else:
        convert=convert+i
if response=='e':
    print("Your encrypted message is:",convert)
else:
    print("Your decrypted message is:",convert)


