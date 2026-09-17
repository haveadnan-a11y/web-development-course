#===================================
##  Pet Profile
#===================================
#function to display pet profile
def pet_profile(name,age,animal):
    print("\n--Pet Profile--")
    print("Name:", name)
    print("Age:", age)
    print("Animal:", animal)
    if age < 5:
        print("This is a young", animal)
    else:
        print("This is an adult", animal)
        #function to give a greeting
def pet_greeting(name):
            print("\nHello", name, "!")
print("Welcome to the pet profile program.")
#get information from the user
pet_name = input("Enter your pet's name: ")
pet_age = int(input("Enter your pet's age: "))
pet_animal = input("Enter your pet's animal type: ")
#call the pet_profile function
pet_profile(pet_name, pet_age, pet_animal)

pet_greeting(pet_name)
print("\nThank you for using the pet profile program!")
