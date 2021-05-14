miles=input ("How many miles did you drive? ")
miles=float(miles) #to make the program recognize miles as a number not a string
def kilometer_function ():#this is the name of my function that converts miles to kilometers
 kilometers= float(miles * 1.6) #1.6 miles equals 1 kilometer
print ("You drove",miles, "miles, which is",kilometers,"kilometers." )
kilometer_function () #calling the function