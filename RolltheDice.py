import random

def roll_dice():
    """Simulates rolling a dice."""
    return random.randint(1, 6)

def dice_rolling_simulator():
    """Runs the dice rolling simulator."""
    print("Dice Rolling Simulator")
    print("----------------------")
    num_rolls = int(input("Enter the number of times to roll the dice: "))

    print("\nRolling the dice...\n")
    for _ in range(num_rolls):
        dice_roll = roll_dice()
        print("Dice rolled:", dice_roll)

dice_rolling_simulator()