#Excercise_3
#My bio
B = {} #Initializes empty dictionary
Data = int(input("Number of users:")) #Prompt to enter amount of data that will be stored
for i in range(Data): #Starts a for loop, which allows the user to input data
    Name = input("Enter your full name:") 
    Age = int(input("Enter your age:")) #Collects user data
    Hometown = input("Enter your hometown:")
    B[Name] = Name,Age,Hometown #prints values in the dictionary
    
print("The users information is as given")
print(B) #Prints List
