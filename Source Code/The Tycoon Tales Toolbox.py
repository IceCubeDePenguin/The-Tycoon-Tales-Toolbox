import locale

def add_commas(number):
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string("%d", number, grouping=True)

items = [
    ("White wool - $1 per item.", 1),
    ("Light Gray wool - $2 per item.", 2),
    ("Gray wool - $5 per item.", 3),
    ("Black wool - $7.5 per item.", 4),
    ("Dark Blue wool - $10 per item.", 5),
    ("Blue wool - $12.5 per item.", 6),
    ("Red wool - $15 per item.", 7),
    ("Green wool - $17.5 per item.", 8),
    ("Yellow wool - $20 per item.", 9),
    ("Hay - $25 per item.", 10),
    ("Melon - $50 per item.", 11),
    ("Pumpkin - $75 per item.", 12),
    ("Bee hive - $100 per item.", 13),
    ("Honey comb - $110 per item.", 14),
    ("Slimeball - $150 per item.", 15),
    ("Magma - $200 per item.", 16),
    ("Gunpowder - $225 per item.", 17),
    ("Prismarine - $250 per item.", 18),
    ("Oak plank - $300 per item.", 19),
    ("Spruce plank - $300 per item.", 20),
    ("Birch plank - $350 per item.", 21),
    ("Jungle plank - $400 per item.", 22),
    ("Acacia plank - $450 per item.", 23),
    ("Dark oak plank - $500 per item.", 24),
    ("Nether star - $600 per item.", 25),
    ("Crimson plank - $700 per item.", 26),
    ("Warped plank - $800 per item.", 27),
    ("Iron ingot - $900 per item.", 28),
    ("Gold ingot - $1,000 per item.", 29),
    ("Diamond - $1,150 per item.", 30),
    ("Amethyst - $1,350 per item.", 31),
    ("Moss - $1,750 per item.", 32),
    ("Mud - $1,900 per item.", 33),
    ("Sculk - $2,000 per item.", 34),
    ("Bone - $3,000 per item.", 35),
    ("Purpur - $4,000 per item.", 36),
    ("Ancient debris - $5,000 per item.", 37),
    ("Red mushroom - $5,500 per item.", 38),
    ("Brown mushroom - $6,000 per item.", 39),
    ("Netherite - $12,000 per item.", 40),
    ("Cherry stairs - $20,000 per item.", 41),
    ("Mosaic bamboo - $40,000 per item.", 42),
    ("Waxed cut copper - $90,000 per item.", 43),
    ("Waxed oxidized copper - $180,000 per item.", 44),
    ("Angler pottery shard - $270,000 per item.", 45)
]

print("Made By IceCubeDePenguin\n")

tools = int(input("What tool do you want to use? (1) Money calculator. (2) Generator finder\n"))

if tools == 1:
    while True:
        try:
            response = int(input("Enter the number of coins per item. (Example: 5000)\n"))

            generators = int(input("Enter the number of specific generator. (Example: 5)\n"))

            generators *= 1
            multiplier = input("Is there 2x coins? (yes/no)\n")

            if multiplier.lower() == 'yes':
                coinsPerMinute = response * 120 / 5 * generators
                coinsPerHour = response * 7200 / 5 * generators
            else:
                coinsPerMinute = response * 60 / 5 * generators
                coinsPerHour = response * 3600 / 5 * generators

            goodCPM = add_commas(coinsPerMinute)
            goodCPH = add_commas(coinsPerHour)

            print("\nYou make " + str(goodCPM) + " coins per minute and " + str(goodCPH) + " coins per hour.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number of coins per item. (Example: 5000)\n")
elif tools == 2:
    def find_item_by_value(value):
        for item_name, item_value in items:
            if item_value == value:
                return item_name
        return "Item not found for given value"

    while True:
        try:
            number = float(input("What generator are you looking for? (1-45):"))
            item = find_item_by_value(number)
  
            print(item)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
else:
    print("Invalid option. Please choose 1 or 2.")

