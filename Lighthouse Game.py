rooms = {
    'Upper Lighthouse': {'South': 'Lower Lighthouse'},
    'Lower Lighthouse': {'North': 'Upper Lighthouse', 'East': 'Den', 'South': 'Walkway', 'West': 'Kitchen'},
    'Den': {'West': 'Lower Lighthouse', 'South': 'Study'},
    'Kitchen': {'East': 'Lower Lighthouse', 'South': 'Side Patio'},
    'Side Patio': {'East': 'Walkway', 'North': 'Kitchen'},
    'Study': {'West': 'Walkway', 'North': 'Den', 'South': 'Hidden Room'},
    'Hidden Room': {'North': 'Study'},
    'Walkway': {'North': 'Lower Lighthouse', 'East': 'Study', 'South': 'Beach', 'West': 'Side Patio'},
    'Beach': {'North': 'Walkway'}
}

nsew = ['North', 'South', 'East', 'West']

items = []

# Introduction
print("\nWelcome to this text based adventure written entirely in Python!\n")
print('***INSTRUCTIONS***')
print('\nThis game relies on your text inputs to play!\n')
print('If in a room with an item you want to pick up: Type "Pick Up".\n')
print('Movement Commands are: North, South, East, West. Remember to capitalize!\n')
print('There are 6 items to Pick Up along your journey. Make sure you are prepared to face whatever waits for you on'
      ' the Beach!\n')
print('To check your Current Room, Inventory, Quest, etc: Type "Status"\n')
print('If you would like to exit, type "Quit"\n')
print('------------------------------------------------------------------------------------')
print('\nYou awake atop a Lighthouse, unaware of how you got there. You sit up, filled with a motivation that\ncannot '
      'be explained. As you rise to your feet, you walk up to the glass walls surrounding your sleeping bag.\n')
print('The stillness of the normally busy beach both calms and frightens you. You must prepare.\n\n')
print('------------------------------------------------------------------------------------')


# Status Input
def show_status():
    print("\nLighthouse Adventure")
    print("Current room: ", currentroom)
    print("Items:", items)
    print("Quest: Collect all 6 Items to protect yourself from whatever is on the Beach, and the Sun!")
    print("Move Commands: North, South, East, West")
    print('Add to Inventory: Type "Pick Up"')
    print('Exit: Type "Quit"')
    return currentroom


# End of Game Win/Lose
def endgame():
    if len(items) == 6:
        print("\n\nYou've prepared well enough, you're ready for anything!\n")
        print("As you step outside, a Giant Crab quickly scuttles from the ocean to face you.\n")
        print("You quickly pull out the Flute and play a lullaby to put the Giant Crab to sleep! It starts to sway,\n"
              "trying to fight the overwhelming urge to sleep. You see your opportunity and swing the Slingshot out of "
              "your pocket and load it with a seashell\nfrom the ground. A quick shot "
              "at the Giant Crab connects to its head! It falls to the sand with a \n\n*CLACK*\n\n*CLACK*\n\n*BOOM*!\n")
        print("You take take the opportunity to rush to fix the Sand Bucket onto its head to make sure it stays asleep."
              "\nThe Rubber Bands are next as you wrap up the Giant Crab's claws, neutralizing its weapons.\n"
              "\nLocals have begun to gather as the momentum shifts.\n")
        print("You motion to the locals for assistance and they begin to help you push the Giant Crab back into the\n"
              "ocean. With your help, the locals have repopulated the beach!\n")
        print("With the help of your Sunscreen and Sunhat, you avoided sunburn. What a great day!\n\n")
        print("You begin to grow exhausted, feeling a yearning to return to the top of the Lighthouse for some rest,\n"
              "something inside you knows that this battle isn't completely over...\n")
        print('------------------------------------------------------------------------------------')
        return "You Succeeded! Congratulations and thanks for playing!\n\nPress Enter to exit."
    else:
        print("\n\nYou have not prepared well enough. Once you step out onto the Beach, the Giant\n"
              "Crab quickly scuttles in front of you. When it sees that you are unprepared,\n"
              "it charges you, scoops you up and throws you a mile out from shore.\n\nYou barely survive.\n")
        print("By the time you swim back to shore, all of the locals have evacuated and the lighthouse claimed by\n"
              "the Giant Crab. A terrible day to try to enjoy the beach!\n")
        print('------------------------------------------------------------------------------------')
        return "You Failed! Thanks for playing and better luck next time!\n\nPress Enter to exit."


# Addresses the room and prompts input
def description(room):
    if room == 'Upper Lighthouse':
        print('\nYou are at the top of the Lighthouse. It is midday and the beach is empty, what for?\n')
        return "You wonder how long you've been here. This place feels familiar, but unknown all the same.\n\n" \
               ">>"
    elif room == 'Lower Lighthouse':
        print("\nOn the bottom end of the spiral stairs that lead downstairs, doors cover every wall. The lower level\n"
              "of the Lighthouse has a classy, Victorian look. Quite odd for a Lighthouse design.\n")
        return 'You see some sunscreen on a table near the bottom of the stairs.\n\n' \
               '>>'
    elif room == 'Kitchen':
        print("\nAs you enter the kitchen, the saltiness of the ocean wades through the open window above the single\n"
              "section sink. It is surprisingly bright as nearly everything in the Kitchen is a very clean white.\n")
        return 'You see a couple Rubber Band balls on the island in the middle of the Kitchen\n\n' \
               '>>'
    elif room == 'Den':
        if 'Slingshot' not in items:
            return '\nThe Den is not much more than a simple lounge area. A fireplace sits the Eastern wall while on' \
                   ' the Northern wall,\nan impressive Slingshot collection hangs, seven in total.\n\n' \
                   '>>'
        else:
            return '\nThe Den, with its three leather chairs and fireplace which lay covered in dust, fills you with' \
                   ' a sense of comfort\nthat you haven\'t felt in a long time. On the Northern wall, an ' \
                   'impressive Slingshot collection hangs, now missing the middle out of seven.\n\n' \
                   '>>'
    elif room == 'Study':
        if 'Flute' not in items:
            print('\nTwo Flutes sit symmetrical on the desk in the Study. A bay window covers the wall behind the\n'
                  'desk, where different national flags hang delicately above it.\n')
            return "Surely whomever owns these Flutes won't miss one.\n\n" \
                   ">>"
        else:
            print('\nOne Flute sits symmetrical to a Flute-shaped dust print. On closer inspection you realize that '
                  'there\'s an inscription near the mouthpiece of the Flute.\n'
                  '"Soon Others Underwater Tread Here."\n')
            return 'You can\'t help but think the ominous inscription is not only an very real warning, but a hidden ' \
                   'message as well.\n\n' \
                   '>>'
    elif room == 'Hidden Room':
        print('\nEtched into the Southern wall of the Study was a crudely drawn Crab. Once touched, the wall\n'
              'shifted, revealing a hidden passageway. Adjourning the walls inside were more crude sketches,\nincluding'
              ' a person sleeping on the Sun, a mob of people rushing into the ocean, and a recipe for a simple Crab '
              'based gumbo.\nAs you pass further into the hallway, you notice a gas torch lit on the wall, right of a '
              'marble altar.\n')
        print('The flickering light reveals a depiction of a giant, 17-foot crustacean, with the same person who was'
              ' drawn\nsleeping on the sun standing in front of it in a defensive stance.\n'
              '\nOn the altar lies a scroll, held down by chunks of marble that have chipped from the altar.\n')
        print("The scroll depicts a long, unending battle between the Lighthouse Keeper and these Giant Crabs. Every\n"
              "42 days, the Giant Crab scuttles onto land, wreaking havoc for humans trespassing into the ocean.\n")
        print("Legend has it that there are Six Synced Singularities that are held by the Lighthouse Keeper,\n"
              "although they may be perceived as normal, everyday items. The items include: a Flute, Sand Bucket,\n"
              "Slingshot, Sunhat, Sunscreen, and Rubber Bands. These Six Singularities act as a beacon of human\n"
              "strength, channeling the unity of humanity to defend their beaches against these crustaceans.\n")
        return "Should the crustacean overtake the Lighthouse and hold any of the Six Singularities, humanity would\n" \
               "be driven away from these beaches for an indefinite period of time, unable to enjoy the oceans in\n" \
               "harmony with the sea-life that calls it home.\n\n" \
               ">>"
    elif room == 'Side Patio':
        if 'Sand Bucket' not in items:
            return '\nIn the Side Patio, you find all kinds of beach toys on the floor and furniture, including a ' \
                   'Sand Bucket.\nA great scene is forming outside as the full moon is rising already.\n\n' \
                   '>>'
        else:
            print('\nIn the Side Patio, you gaze outside to a beautiful scene where the forest meets the ocean.\n')
            return 'Even though it is midday, you can see the full moon rising above the treeline.\n\n' \
                   '>>'
    elif room == 'Walkway':
        if 'Sunhat' not in items:
            return '\nIn the walkway, doors surround you on every side. Many pairs of sandals and water-shoes ' \
                   'scatter\nthe ground in an effort to not track in sand, even though it still finds its way ' \
                   'everywhere.\nIn front of you there is a coat stand with a Sunhat on top.\n\n' \
                   '>>'
        else:
            print('\nIn the walkway, doors surround you on every side. Many pairs of sandals and water-shoes scatter\n'
                  'the ground in an effort to not track in sand, even though it still finds its way everywhere.\n')
            return "The door outside stands to the South, are you fully prepared to see whatever is outside?\n\n" \
                   ">>"
    elif room == 'Beach':
        return endgame()
    else:
        return room


# Moves the current room
def whereami(room, direction):
    here = rooms[room]
    if direction == 'Pick Up':
        return room
    elif direction == 'Status':
        return show_status()
    elif direction not in here:
        print('Invalid Input!')
        return room
    else:
        print('\nYou are moving to the {}!'.format(here[direction]))
        return here[direction]


# Picking Up Items
def pickup(room):
    if room == 'Lower Lighthouse':
        if 'Sunscreen' not in items:
            items.append('Sunscreen')
            print("\nYou put on Sunscreen!\n")
        else:
            print("\nYou already put on sunscreen, you don't need more!\n")
    elif room == 'Den':
        if 'Slingshot' not in items:
            items.append('Slingshot')
            print("\nYou pick up a Slingshot!\n")
        else:
            print("\nYou already have a Slingshot; ranged weapons cannot be dual-wielded!\n")
    elif room == 'Kitchen':
        if 'Rubber Bands' not in items:
            items.append('Rubber Bands')
            print("\nYou pick up Rubber Bands!\n")
        else:
            print("\nYou already picked up a ball of Rubber Bands, that should be enough!\n")
    elif room == 'Side Patio':
        if 'Sand Bucket' not in items:
            items.append('Sand Bucket')
            print("\nYou pick up a Sand Bucket!\n")
        else:
            print("\nYou already have a Sand Bucket!\n")
    elif room == 'Study':
        if 'Flute' not in items:
            items.append('Flute')
            print("\nYou pick up a Flute!\n")
        else:
            print("\nYou already have a Flute!\n")
    elif room == 'Walkway':
        if 'Sunhat' not in items:
            items.append('Sunhat')
            print("\nYou put on a Sunhat!\n")
        else:
            print("\nYou are already wearing a Sunhat!\n")
    else:
        print("\nThere is nothing to Pick Up here.\n")


# Main Console
if __name__ == '__main__':

    currentroom = "Upper Lighthouse"

    stop = 'go'

    while stop != 'Quit':
        user_input = input(description(currentroom))

        if user_input == 'Quit' or currentroom == 'Beach':
            break

        # Determining Function based on Input
        if currentroom == "Upper Lighthouse":
            currentroom = whereami("Upper Lighthouse", user_input)
        elif currentroom == "Lower Lighthouse":
            if user_input == 'Pick Up':
                pickup(currentroom)
            currentroom = whereami("Lower Lighthouse", user_input)
        elif currentroom == "Den":
            if user_input == 'Pick Up':
                pickup(currentroom)
            currentroom = whereami("Den", user_input)
        elif currentroom == "Kitchen":
            if user_input == 'Pick Up':
                pickup(currentroom)
            currentroom = whereami("Kitchen", user_input)
        elif currentroom == "Side Patio":
            if user_input == 'Pick Up':
                pickup(currentroom)
            currentroom = whereami("Side Patio", user_input)
        elif currentroom == "Study":
            if user_input == 'Pick Up':
                pickup(currentroom)
            currentroom = whereami("Study", user_input)
        elif currentroom == "Walkway":
            if user_input == 'Pick Up':
                pickup(currentroom)
            currentroom = whereami("Walkway", user_input)
        elif currentroom == "Hidden Room":
            currentroom = whereami('Hidden Room', user_input)
        else:
            print("Invalid!\n")
