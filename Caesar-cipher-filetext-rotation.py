import time
import os
#This will prompt user either to keep or remove orginal file
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

#asking users either to keep or delete the orginal file !!
ask_user=input('"Press "k" to keep the orginal file/ "D for deleting the orginal file').lower()
if ask_user=="k":
    askuser=input("Enter the name of the rotated file you wish to save as : ")
    print("Please wait !! Just a sec .......")
    time.sleep(3)
    print("The rotated file has been saved in Download directory !! ")
    with open (fr"C:\Users\Dell\Downloads\{askuser}","w") as file1 :
        file1.write(output_message)
    print("Saved successfully !!")
if ask_user=="d":
    os.remove(filename)
    print("Wait !! The original file is being removed from the system !")
    time.sleep(3)
    askuser=input("Enter the name of the rotated file you wish to save as : ")
    print("Please wait !! Just a sec .......")
    time.sleep(3)
    print("The rotated file has been saved in Download directory !! ")
    with open (fr"C:\Users\Dell\Downloads\{askuser}","w") as file1 :
        file1.write(output_message)
else :
    print('Select either "k" or "D"!! dumb idiot ')
