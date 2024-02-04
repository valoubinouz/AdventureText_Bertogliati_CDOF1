def handle_talk():
    print("You start talking to the crow.")
    print("After introducing yourself, what do you ask him?")
    print("Do you ask him about his wife and kid, or do you compliment him on his voice?")

    while True:
        talk_choice = input("Enter 'wife and kid' or 'compliment': ").lower()
        if talk_choice == "wife and kid":
            print("The crow gets scared for his family and flies away with the cheese!")
            print("You lost...")
            break
        elif talk_choice == "compliment":
            print("You chose to compliment the crow on his voice...")
            print("The crow loves the compliment! He trusts you.")
            print("He lets the cheese fall while singing for you!")
            print("Good job, you have successfully gotten the cheese!")
            break
        else:
            print("Invalid choice. Please enter 'wife and kid' or 'compliment'.")

def handle_climb():
    print("You chose to climb the tree.")
    print("As you are climbing, the crow gets scared and flies away.")
    print("You lost :(")

def main():
    print("Welcome to the crow and the fox fairytale!")
    print("You are the smart fox, trying to get the cheese from the crow's mouth.")
    print("As the fox, you have to use tricks to steal the cheese.")
    print("The crow is currently on top of a tree, looking down on you.")
    print("Do you want to talk to the crow or climb the tree?")

    while True:
        first_choice = input("Enter 'climb' or 'talk': ").lower()
        if first_choice == "talk":
            handle_talk()
            break
        elif first_choice == "climb":
            handle_climb()
            break
        else:
            print("Invalid choice. Please enter 'climb' or 'talk'.")

if __name__ == "__main__":
    main()
