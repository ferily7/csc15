#This function gets the user inputs and implements them in the song
def singOldMcD(animal,sound):
    chorus()
    print("And on that farm he had a", animal, "Ee-igh, Ee-igh, Oh!")
    print("With a", sound, sound, "here and a", sound, sound, "there.")
    print("Here a", sound, "there a", sound, "everywhere a", sound, sound)
    chorus()

#This function prints the chorus of the song
def chorus():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    
def main():

    #Initialize variables
    animal = input("Enter a animal: ")
    sound = input("Enter a sound: ")
    #Declares function
    singOldMcD(animal,sound)

main()
