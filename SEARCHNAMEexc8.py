#Excercise_8
#SearchName
#initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Get user input to search for the name in the list
search_name = input("Enter the name to search for: ").strip()

#If else to search if name is already entered in the list
if search_name in names:
    print(f"{search_name} is in the list.")
else:
    print(f"{search_name} was not found in the list.")
