import time
import base64
filename=input("Enter the name of file or provide full path if raised error :").strip(' " ')
output_message=""
with open (fr'{filename}','r') as file :
    content=file.read()
    for i in range(len(content)):
     x=content[i]
     encoded_textbefore = base64.b64encode(x.encode('utf-8'))  # Convert to bytes, then base64
     encoded_text = encoded_textbefore.decode()  # Convert bytes to string for readable output
     output_message+=encoded_text
askuser=input("Enter the name of the rotated file you wish to save as : ")
print("Please wait !! Just a sec .......")
time.sleep(3)
print("The encrypted file has been saved in Download directory !! ")
with open (fr"C:\Users\Dell\Downloads\{askuser}","w") as file1 :
    file1.write(output_message)
print("Saved successfully !!")