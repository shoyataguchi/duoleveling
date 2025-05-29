import sys

######################
### Configurations ###
######################
CARD_SIZE = 5
COLUMN_LETTERS = ("B", "I", "N", "G", "O")
MAX_BINGO_NUMBER = 75
FREE_SPACE_MARKER = "FREE"
MARK_CHARACTER = "XX"

###################
### Validations ###
###################

# Run the validation. Returns False if validation fails. Returns True if all validations pass.
def validate():
    print("Validating config values...")
    if CARD_SIZE <= 0:
        print(f"card size need to be >0, got {CARD_SIZE}.")
        return False

    # checking if the CARD_SIZE is an odd number
    if CARD_SIZE % 2 == 0:
        print(f"card size need to be a odd number, got {CARD_SIZE}")
        return False

    if CARD_SIZE != len(COLUMN_LETTERS):
        print(f"card size need to be same as the length of column letters, got card size: {CARD_SIZE}, column letters: {COLUMN_LETTERS}")
        return False

    return True

# Prints a bingo card.
def display_card(card):
    print("Printing a bingo card...\n")
    print("Not yet implemented!")

#################
### Main code ###
#################

# Run validate(). If the returned value is false, exit the program.
if not validate():
    sys.exit()

print("Config values are valid!")

# Prepare 5x5 list of lists
dummy_card = [
    [7, 22, 31, 50, 68],
    [3, 18, 42, 58, 71],
    [12, 29, -1, 47, 62],
    [9, 16, 35, 53, 75],
    [1, 25, 40, 49, 61]
]
# Print the card.
display_card(dummy_card)
