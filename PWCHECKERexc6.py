#Excercise_6
#Password Checker
CorrectPW = "12345"

# Function to check password
def password_checker():
    while True:
        # Ask the user to input the password
        GivePW = input("Please input your password: ")
        
        # Check if the entered password is correct
        if GivePW == CorrectPW:
            print("You are successfully logged in")
            break  
        else:
            print("The password is incorrect. Please try again.")

# Run the password checker
password_checker()


