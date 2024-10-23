#Excercise_10
#Determine the Even or Odd checker function 
def even_odd_checker(inputnumber): #Defines function which contains one parameter (inputnumber)
    if inputnumber % 2 == 0:
        return f"{inputnumber} is even."
    else:
        return f"{inputnumber} is odd." #Checks if entered number is even or odd

def main(): #Main function 
    input_number = int(input("Enter the number: ")) #Promps text for user to input a number
    input_number = int(input_number) 
    result = even_odd_checker(input_number)  #Calls back even_odd_checker within input_number
    print(result)  

if __name__ == "__main__":
    main() #Calls back main function to run the program

   


