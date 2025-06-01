import time
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
output_message=""
#asking user to input text 
userinput=input("Enter the text to be rotated :").upper().strip()
#asking the shift digit also 
print("If A is rotated by 3 digits it becomes D :")
#explaining what shift does 
time.sleep(1)
print("If B is rotated by 3 digits it becomes E :")
time.sleep(1)
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