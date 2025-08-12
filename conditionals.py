userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")
    userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
    if userReply == "stamps":
        print("We have many stamps design to choose from.")
    elif userReply == "envelope":
        print("We have many envelope sizes to choose from.")
    elif userReply == "copy":
        try:
            copies = int(input("How many copies would you like? (Enter a number) "))
            print("Here are {} copies.".format(copies))
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Thank you, please come again.")
    
else:
    print("Please come back when you need to ship a package. Thank you.")

