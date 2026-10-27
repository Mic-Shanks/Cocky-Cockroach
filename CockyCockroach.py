#Michael Shanks

import random

#Room dictionary
rooms = {
    'Garage': {'north': 'Laundry Room', 'west': 'Kitchen'},
    'Laundry Room': {'Exit', 'Human'},
    'Kitchen': {'west': 'Pantry', 'east': 'Garage', 'south': 'Hallway', 'north': 'Living Room'},
    'Pantry': {'east': 'Kitchen'},
    'Hallway': {'north': 'Kitchen', 'east': 'Bedroom'},
    'Bedroom': {'west': 'Hallway'},
    'Living Room': {'south': 'Kitchen', 'east': 'Bathroom'},
    'Bathroom': {'west': 'Living Room'}
}

#Item dictionary
items = {
    'Garage': 'Kernel',
    'Kitchen': 'Noodle',
    'Pantry': 'Sugar',
    'Hallway': 'Meat',
    'Bedroom': 'Cookie',
    'Living Room': 'Bread',
    'Bathroom': 'Candy'
}
#Room Descriptions
descriptions = {
    'Garage': 'The room is a cramped two-car Garage transformed into a chaotic realm of creativity, with mismatched shelves stacked\n'
              'with tools and half-finished projects. The faint scent of lingering motor oil pervades the room, while the soft hum of\n'
              'an old refrigerator adds a low background buzz that feels oddly comforting.',
    'Kitchen': 'The Kitchen is bright, adorned with an assortment of shiny appliances and rustic wood cabinets. The warm scent of cinnamon\n'
               'intertwines with the sweet aroma of baked cookies, creating an inviting atmosphere.',
    'Pantry': 'The Pantry is a small, dimly lit room tucked behind a narrow door, its shelves brimming with an assortment\n'
              'of jars and bags. The air is thick with the aroma of old herbs and a faint, musty sweetness, reminiscent\n'
              'of dried fruits. ',
    'Hallway': 'The Hallway is a narrow corridor lined with polished oak paneling that gleams in the soft glow of vintage sconces, which cast gentle\n'
               'shadows across the faded family photographs adorning the walls. A faint, nostalgic aroma of lavender and cedar lingers in the air,\n'
               'punctuated by the distant, rhythmic ticking of an ornate grandfather clock echoing with each passing minute.',
    'Bedroom': 'The Bedroom is adorned with soft pastel colors.  The gentle hum of a nearby ceiling fan mingles with the sweet aroma of lavender,\n'
               'creating a calming atmosphere perfect for relaxation or creativity. A whimsical mural of an enchanted forest sprawls across\n'
               'one wall, and on the bedside table a curious old music box sits silently, its intricately carved lid adorned with tiny animals.',
    'Living Room': 'This room is a snug Living Room adorned with soft, oversized furniture that invites lounging, its walls lined with\n'
                   'shelves filled with an eclectic mix of books and framed photographs. The air is infused with the faint aroma of\n'
                   'vanilla candles, while gentle indie music plays softly in the background, creating a welcoming ambiance.',
    'Bathroom': 'The bathroom is surprisingly spacious, adorned with glimmering white tiles that give it a sense of cleanliness\n'
                'yet offer hints of overdue maintenance in the caulked edges. The sharp scent of lavender air freshener mingles\n'
                'with the faintest trace of mildew, creating an oddly comforting yet slightly stale atmosphere.',

}

#Initializing inventory list
inventory= []


#Opening Logo
def logo():
    print("Welcome to:")
    print(" ___              |")
    print("|    \\            |")
    print("|                 | /  |   |")
    print("|       ___   __  |/   |   |")
    print("|    / |   | |    |\\    ---|")
    print("|___/   ---   --  | \\    __|")
    print("                    COCKROACH")
    print("                           Ver: 0.1")
    print("\n")
    print("Rush to feed your family, but watch out for those pesky humans!")
    print('')
    print("Type 'help' for commands")
    print("\n")

#Starting room
room = 'Garage'

#Function to move rooms.
def movePlayer(room, direction):
    human = random.randint(1, 8)
    if direction in rooms[room]:
        room = rooms[room][direction]
        print('You are in the {}.'.format(room))
        if human == 1:
            print("A human moves about, doing tasks.")
        else:
            print("There is no movement.")
    else:
        print("That is not a valid direction.")
    return room, human

#Function to acquire items
def takeItem(room, item):
    if item in items[room].lower():
        print('You got {}!'.format(item))
        inventory.append(item)
        items[room] = 'nothing'
    else:
        print("You do not see that item here.")

#Function for being spotted
def death(human):
    if human == 1:
        print('The human turns and sees you, shrieks loudly, and stomps on you with their foot!')
        print('GAME OVER!  You died!')
        exit = end()
    else:
        exit = False
    return exit

#Function to show room description
def roomDesc(room):
    exits = list(rooms[room].keys())
    item = items[room]
    print(descriptions[room])
    if item == 'nothing':
        print('There is nothing on the floor')
    else:
        print('There is a {} on the floor.'.format(items[room]))
    print("Exits:", exits)

#Exit function
def end():
    print('\nThanks for playing!')
    input()
    exit = True
    return exit

#Main code
logo()
print("You are in the {}.".format(room))
choice = ''
exit = False
human = 0
while exit != True:
    choice = input('Command:\n').lower()
    if choice == 'exit':
        exit = end()
    elif choice.lower() == 'help':
        print('COMMANDS:\n\n'
              "To move rooms, type 'go' and the direction that you wish to move.\n\n"
              "To take an item, type 'take' and the item you wish to take.\n\n"
              "To check your inventory, type 'inventory'.\n\n"
              "Type 'look' to look around the room.\n\n"
              "To exit, type 'exit'.\n")
    elif choice == 'look':
        if human == 1:
            exit = death(human)
        else:
            roomDesc(room)
    elif choice == 'inv' or choice == 'inventory':
        if human == 1:
            exit = death(human)
        else:
            print('Inventory:', inventory)
    elif choice.startswith('go'):
        choice = choice.split()
        lower_move = {key.lower(): value for key, value in rooms.items()}
        move = choice[1]
        room, human = movePlayer(room, move)
        if room == 'Laundry Room' and len(inventory) == 7:
            print('You scurry to your home quickly, where all of your children welcome you happily!\n')
            print('CONGRATULATIONS!  Your family is fed!')
            exit = end()
        elif room == 'Laundry Room' and len(inventory) != 7:
            print('While you scurry about looking for food, the human notices you and squishes you with their foot!')
            print('GAME OVER!  You died!')
            exit = end()
    elif choice.startswith('take'):
        if human == 1:
            exit = death(human)
        else:
            choice = choice.split()
        item = choice[1]
        print(item)
        takeItem(room, item)
    else:
        print("Invalid command.")