import time
filename=input("Enter the name of file or provide full path if raised error :").strip(' " ')
shift=int(input("Enter the shift value also :"))
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
output_message=""
with open (fr'{filename}','r') as file :
    content=file.read().upper()
    for i in range(0,len(content)):
        x=content[i]
        if x in alphabet :
            location=alphabet.find(x)
            new_location=(location+shift)%26
            output_message+=alphabet[new_location]
        else :
            output_message+=x
askuser=input("Enter the name of the rotated file you wish to save as : ")
print("Please wait !! Just a sec .......")
time.sleep(3)
print("The rotated file has been saved in Download directory !! ")
with open (fr"C:\Users\Dell\Downloads\{askuser}","w") as file1 :
    file1.write(output_message)
print("Saved successfully !!")