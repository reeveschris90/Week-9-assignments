import os #imports os library
directory= input ("Which directory would you like to save your file in? ")
file = input ("What is the name of your file? ") #file name
os.path.isdir (directory)
name = input ("What is your name? ") #user's name
address = input("What is your address? ")#user's address
phone_number = input ("What is your phone number? ")#user's phone number
with open (file, 'w') as file_object: #open it up to write and read
 file_object.write( name )
 file_object.write(" , ")
 file_object.write( address )
 file_object.write(" , ")
 file_object.write( phone_number )


with open (file, 'r') as file_object:#to read from the file
 data = file_object.read()
 print (data)#shows the data for verification
