print("hello")
print("Welcome to valoubinouz adventure game")

### Print a welcome message
print("Welcome to the the crow and the fox fairytale !")
print("You are a the smart fox, tryning to get the cheese from the crow mouth.")
print("As the fox you have to use tricks to steal the cheese")
print("The crow is currently on top of tree, looking down on you")
print("Do you want to talk to the crow or climb to the tree ?")

### Prompt user for a choice
firstChoice = input("enter \"climb\" or \"talk\" : ")

if(firstChoice == "talk"):
  print("You start talking to the crow")
  print("After introducting yourself, what do you ask him ? ")
  print("You ask him about his wife and kid Or you compliment him on his voice ?")

  talkChoice = input("enter \"wife and kid\" or \"compliment\" : ")

  if(talkChoice == "wife and kid"):
    print("The crow get scared for his family and flies away with the cheese ! ")
    print("You lost...")
  elif(talkChoice == "compliment"):
    print("You chose to compliment the crow on his voice...")
    print("The crow loves the compliment !, he trust you ")
    print("he let the cheese fall while singing for you ! ")
    print ("Good Job, you have successfully gotten the cheese back ! ")
  else:
    print("Invalid choice. Please enter 'wife and kid' or 'compliment'")

elif(firstChoice == "climb"):
  print("You chose to climb the tree")
  print("As you are climbing, The crow get scared and fly away")
  print("You lost :(")

else:
  print("Invalid choice. Please enter climb or talk")