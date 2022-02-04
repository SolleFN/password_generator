from random import randint
import pyperclip

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',0,1,2,3,4,5,6,7,9,"@","#","_"]

while True:
    answer = input("Vuoi generare una password ? S o N --> ")
    if answer == "S" or answer == "s":
        i = 0
        password = []
        passwords = ''
        question = int(input("Inserire la lunghezza della password (Max 22) --> "))
        while i <= question:
            password.append(str(characters[randint(0,len(characters))]))
            i += 1
        passwords = passwords.join(str(e)for e in password)
        print(f"Password copiata , premere CTRL + V o incolla per incollarla!")
        pyperclip.copy(passwords)
        
    else:
        break