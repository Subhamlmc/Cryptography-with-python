import time
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
output_message="" 
userinput=input("Enter the text to be rotated :").upper().strip()
print("If A is rotated by 3 digits it becomes D :")
print("If B is rotated by 3 digits it becomes E :")
shift=int(input("Enter the shift digit also :"))
for i in range(0,len(userinput)):
    x=userinput[i]
    if x in alphabet :
     location=alphabet.find(x)
     new_location=(location+shift)%26
     output_message+=alphabet[new_location]
    else :
        output_message+=x

print(f"The output of the text you provided is {output_message}")
