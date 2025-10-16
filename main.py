import random

print("\nPassMate - Made by Edro\nA program that lets you generate random passwords to use.\n")

words = ["Apple", "Ball", "Cat", "Dog", "Elephant", "Flower", "Giraffe", "House", "Ice", "Jungle", "Kite", "Lamp",
         "Mountain", "Nest", "Ocean", "Planet", "Queen", "Rocket", "Sun", "Tree", "Umbrella", "Van", "Window",
         "Xylophone", "Yacht", "Zebra", "Acorn", "Button", "Cup", "Door", "Egg", "Fish", "Garden", "Hat", "Island",
         "Jacket", "King", "Leaf", "Moon", "Nail", "Orange", "Piano", "Quilt", "Rose", "Star", "Telephone",
         "Universe", "Vine", "Wave", "Xenon", "Yellow", "Zipper", "Angel", "Balloon", "Cloud", "Dream", "Echo",
         "Feather", "Glow", "Hive", "Icicle", "Jump", "Kitten", "Lemonade", "Maple", "Nose", "Owl", "Patch",
         "Quiver", "Silver", "Tides", "Unicorn", "Vessel", "Wild", "Zodiac", "Actor", "Candle", "Dreamer", "Edge",
         "Firework", "Gate", "Helmet", "Joy", "Lantern", "Night", "Paradox", "Quest", "Sunflower", "Tide", "Umbra",
         "Vineyard", "Extra", "Yonder", "Zinnia", "Anchor", "Bread", "Castle", "Falcon", "Ghost", "Hail", "Insect",
         "Ladder", "Mist", "Nostalgia", "Pond", "Quicksand", "Ship", "Voyage", "Wonder", "Zephyr", "Circle",
         "Firefly", "Gem", "Hummingbird", "Ivy", "Journey", "Kangaroo", "Lighthouse", "Meadow", "Orbit", "Penguin",
         "Quake", "Sea", "Turtle", "Wind", "Barrel", "Frolic", "Horizon", "Infinity", "Jewel", "Love", "Moonlight",
         "Nestle", "Quiver", "Ripple", "Spark", "Train", "Velvet", "Willow", "Xeno", "Zoo", "Adventure", "Breeze",
         "Captain", "Dragon", "Eclipse", "Goose", "Harvest", "Iceberg", "Joyful", "Kangaroo", "Lighthouse",
         "Mystery", "Nebula", "Oasis", "Pirate", "Quartz", "Rainbow", "Shimmer", "Titan", "Utopia", "Voyage",
         "Whale", "Xenial", "Yacht", "Zephyr", "Alpine", "Biscuit", "Candle", "Dolphin", "Eagle", "Forest", "Galaxy",
         "Helix", "Ivory", "Jackal", "Kaleidoscope", "Lynx", "Meteor", "Nectar", "Ocelot", "Pineapple", "Quasar",
         "Rosemary", "Sapphire", "Tornado", "Unicorn", "Vortex", "Willow", "Xplorer", "Yellowstone", "Zebra",
         "Amethyst", "Banana", "Clarity", "Dewdrop", "Elixir", "Frost", "Gale", "Hedgehog", "Indigo", "Jaguar",
         "Knot", "Lumen", "Moonstone", "Nova", "Oasis", "Pine", "Quiver", "Rustic", "Snowflake", "Tango", "Ultra",
         "Violet", "Wander", "Xenon", "Yonder", "Zigzag", "Acorn", "Breeze", "Cascade", "Dragonfly", "Echo",
         "Frostbite", "Glacier", "Horizon", "Iridescent", "Jubilee", "Kite", "Lunar", "Mistral", "Nebula", "Ocean",
         "Puppy", "Quench", "Ripple", "Seashell", "Tide", "Umbra", "Valley", "Wildflower", "Xenial", "Yarn",
         "Zenith", "Abyss", "Blossom", "Cove", "Dawn", "Element", "Fern", "Glade", "Harmonica", "Impression",
         "Journey", "Knot", "Lush", "Meadow", "Nymph", "Oath", "Petal", "Quest", "Reverie", "Solstice", "Tundra",
         "Undertow", "Vista", "Windfall", "Xylograph", "Yellow", "Zinc", "Amber", "Brook", "Cactus", "Dove", "Eagle",
         "Flare", "Glimmer", "Harbor", "Inkwell", "Jade", "Knot", "Lagoon", "Magma", "Nest", "Opal", "Pinecone",
         "Quartz", "Reef", "Swirl", "Timber", "Urchin", "Vervain", "Whirlpool", "Xylene", "Yonder", "Zenith",
         "Alabaster", "Breeze", "Chime", "Dawn", "Eden", "Fog", "Grove", "Haven", "Ice", "Jewel", "Kaleidoscope",
         "Lagoon", "Moss", "Nectar", "Pine", "Quiet", "Raven", "Sway", "Tonic", "Umbra", "Veil", "Whispers",
         "Xenon", "Yew", "Zinnia", "Astonish", "Breathe", "Chill", "Desire", "Eclipsed", "Flicker", "Glimpse",
         "Hollow", "Inspire", "Journey", "Lark", "Mystic", "Nestle", "Oscillate", "Pulse", "Quell", "Rise",
         "Shiver", "Tremor", "Uprise", "Vivid", "Wander", "Xplore", "Yield", "Zest"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "-", ",", ".", "/", ":", ";", "<", ">", "=", "?", "@", "[",
           "]", "\\", "^", "_", "{", "}", "|", "~"]

alphabetic_characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def all_char_digits(a):
    z = 0
    for x in a:
        for y in range(0, 10):
            if x == str(y):
                z += 1
    if z != len(a):
        return False
    return True

first_input = input('Would you like to generate regular passwords "r" or passphrases "p"?\n> ').lower()

while first_input != "r" and first_input != "p":
    first_input = input('Please specify a valid value\nWoud you like to generate a regular password "a" or a passphrase'
                    ' "b"?\n> ').lower()

if first_input == "r":
    input_a = input("How many passwords would you like to generate?\n> ")
else:
    input_a = input("How many passphrases would you like to generate?\n> ")

while input_a == ''or all_char_digits(input_a) == False or int(input_a) < 1 :
    if first_input == "r":
        input_a = input("Please specify a valid value\nHow many passwords would you like to generate?\n> ")
    else:
        input_a = input("Please specify a valid value\nHow many passphrases would you like to generate?\n> ")

if first_input == "r":
    input_b = input("Could you specify the length of the password(s)?\n> ")
else:
    input_b = input("Could you specify the amount of words to include in the passphrase(s)\n> ")

while input_b == ''or all_char_digits(input_b) == False or int(input_b) < 1 :
    if first_input == "r":
        input_b = input("Please specify a valid value\nCould you specify the length of the password(s)?\n> ")
    else:
        input_b = input("Please specify a valid value\nCould you specify the amount of words to include in the passphrase(s)\n> ")

if first_input == "r":
    if int(input_a) == 1:
        input_c = input("Would you like to generate a mixed password or specify what should it include? (m for Mixed, s for Specify).\n> ").lower()
    else:
        input_c = input("Would you like to generate mixed passwords or specify what should they include? (m for Mixed, s for Specify).\n> ").lower()
    while input_c != "m" and input_c != "s":
        if int(input_a) == 1:
            input_c = input("Please specify a valid value\nWould you like to generate a mixed password or specify what should it include? (m for Mixed, s for Specify).\n> ").lower()
        else:
            input_c = input("Please specify a valid value\nWould you like to generate mixed passwords or specify what should they include? (m for Mixed, s for Specify).\n> ").lower()
else:
    input_c = input("If you would like your words to be separated using a separator, please indicate one; if not, leave the below input empty.\n> ")
    print('')
    for x in range(0, int(input_a)):
        a = ""
        for y in range(0, int(input_b)):
            a += random.choice(words) + (input_c if y != int(input_b) - 1 else '')
        print(a)

if first_input == "r":
    if input_c == "m":
        print('')
        for x in range(0, int(input_a)):
            a = ""
            for y in range(0, int(input_b)):
                z = random.randint(0, 2)
                match z:
                    case 0:
                        a += str(random.randint(0, 9))
                    case 1:
                        w = random.randint(0, 1)
                        if w == 0:
                            a += random.choice(alphabetic_characters)
                        else:
                            a += random.choice(alphabetic_characters).lower()
                    case 2:
                        a += random.choice(symbols)
            print(a)
    else:
        input_d = input('Do you want to include alphabetic characters in the password(s)? Type "y" for Yes or "n" for No.\n> ').lower()
        while input_d != "y" and input_d != "n":
            input_d = input('Please specify a valid value\nDo you want to include alphabetic characters in the password(s)? Type "y" for Yes or "n" for No.\n> ').lower()
        input_e = input('Do you want to include numbers in the password(s)? Type "y" for Yes or "n" for No.\n> ').lower()
        while input_e != "y" and input_e != "n":
            input_e = input('Please specify a valid value\nDo you want to include numbers in the password(s)? Type "y" for Yes or "n" for No.\n> ').lower()
        input_f = input('Do you want to include symbols in the password(s)? Type "y" for Yes or "n" for No.\n> ').lower()
        while input_f != "y" and input_f != "n":
            input_f = input('Please specify a valid value\nDo you want to include symbols in the password(s)? Type "y" for Yes or "n" for No.\n> ').lower()
        while input_d == "n" and input_e == "n" and input_f == "n":
            input_f = input("You've excluded letters and numbers from the password(s), so symbols are required"
                            " - otherwise, the password(s) would be empty.\nPlease specify"
                            " Yes: \"y\".\n> ").lower()
        print('')
        for x in range(0, int(input_a)):
            y = int(input_b)
            z = ""
            tries = 0
            while y > 0:
                 w = random.randint(0, 3)
                 match w:
                     case 0:
                         if input_d == "y":
                             z += random.choice(alphabetic_characters)
                             y -= 1
                     case 1:
                         if input_e == "y":
                             z += str(random.randint(0, 9))
                     case 2:
                         if input_f == "y":
                             z += random.choice(symbols)
                             y -= 1
            print(z)
