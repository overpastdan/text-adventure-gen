import random

def create_adventure():
    hero = input("Enter the name of your hero: ")
    lives = 3

    monsters = ["Goblin", "Orc", "Skeleton", "Dark Mage", "Spider Queen"]

    print("\nYour adventure begins!")
    print(f"{hero} stands at the bottom of the Tower of Trials. The goal: reach the top and claim eternal glory.\n")
    print(f"{hero} has {lives} lives.\n")

    floor = 1
    while floor <= 3:
        print(f"--- Floor {floor} ---")
        monster = random.choice(monsters)
        print(f"As {hero} climbs higher, a {monster} appears and blocks the way!")

        choice = input("Do you fight or flee? (fight/flee): ").lower()

        if choice == "fight":
            outcome = "win" if random.random() < 0.7 else "lose"  # 70% chance to win
            if outcome == "win":
                print(f"{hero} bravely defeats the {monster}!\n")
                floor += 1  # Move to next floor
            else:
                lives -= 1
                print(f"The {monster} wounded {hero}! Lives remaining: {lives}\n")
                if lives == 0:
                    print(f"{hero} has no lives left...")
                    print("GAME OVER")
                    return

        elif choice == "flee":
            escape = "free" if random.random() < 0.3 else "caught"  # 30% clean escape
            if escape == "free":
                print(f"{hero} successfully fled from the {monster} and advanced to the next floor!\n")
                floor += 1
            else:
                print(f"{hero} tried to flee but ran into another monster!\n")
                # New monster encounter without advancing floor
        else:
            print(f"{hero} hesitated and the {monster} attacked!")
            lives -= 1
            print(f"In the confusion, {hero} was wounded! Lives remaining: {lives}\n")
            if lives == 0:
                print(f"{hero} has no lives left...")
                print("GAME OVER")
                return

    print(f"🏆 Congratulations! {hero} has conquered all three floors and reached the top of the Tower of Trials!")

if __name__ == "__main__":
    create_adventure()
