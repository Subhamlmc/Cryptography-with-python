import time
import base64
filename=input("Enter the name of file or provide full path if raised error :").strip(' " ')
output_message=""
with open (fr'{filename}','r') as file :
    content=file.read()
    for i in range(len(content)):
     x=content[i]
     encoded_textbefore = base64.b64decode(x.decode('utf-8'))  # Convert to bytes, then base64
     decoded_text = encoded_textbefore.encode()  # Convert bytes to string for readable output
     output_message+=decoded_text
askuser=input("Enter the name of the rotated file you wish to save as : ")
print("Please wait !! Just a sec .......")
time.sleep(3)
print("The decrypted file has been saved in Download directory !! ")
with open (fr"C:\Users\Dell\Downloads\{askuser}","w") as file1 :
    file1.write(output_message)
print("Saved successfully !!")