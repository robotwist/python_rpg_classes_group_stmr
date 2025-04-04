from character import Character
from monster import Monster, Attack, Loot
from weapon import Weapon
from potion import Potion
from spell import Spell
from shop import Shop
import random

def main():
    # Create player character
    print("Welcome to Python RPG!")
    player_name = input("What is your name, adventurer? ")
    player = Character(player_name, 100, mana=80, level=1)
    player.gold = 50  # Starting gold
    
    # Give player starting equipment
    starter_weapon = Weapon("Rusty Sword", "An old but functional sword", 5, 10)
    health_potion = Potion("Small Health Potion", "Restores a little health", 10, "heal", 15)
    
    # Add items to inventory
    player.inventory = [health_potion]
    player.equip_weapon(starter_weapon.name)
    
    # Learn a basic spell
    fireball = Spell("Fireball", 15, mana_cost=10, effect="burn")
    player.learn_spell(fireball)
    
    print(f"\nYou are {player}. Your adventure begins!\n")
    
    # Game loop
    while player.is_alive():
        # Menu
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Visit shop")
        print("3. Check inventory")
        print("4. Check status")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            explore(player)
        elif choice == "2":
            visit_shop(player)
        elif choice == "3":
            check_inventory(player)
        elif choice == "4":
            print(player)
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, try again.")
    
    if not player.is_alive():
        print("You have been defeated! Game over.")

def explore(player):
    # Random chance of encounter
    if random.random() < 0.7:  # 70% chance of monster
        # Create random monster based on player level
        monster_types = ["Goblin", "Wolf", "Skeleton", "Orc", "Dragon"]
        monster_level = min(len(monster_types) - 1, player.level - 1)
        monster_type = monster_types[max(0, monster_level)]
        
        monster_health = 20 + (player.level * 10)
        monster = Monster(monster_type, monster_health)
        
        # Create monster attack
        attack_damage = 5 + (player.level * 2)
        monster_attack = Attack(f"{monster_type} Attack", attack_damage)
        
        print(f"\nYou encountered a {monster_type} with {monster_health} health!")
        
        # Combat loop
        while monster.health > 0 and player.is_alive():
            # Player turn
            print("\nYour turn!")
            print("1. Attack with weapon")
            print("2. Cast a spell")
            print("3. Use an item")
            print("4. Run away")
            
            action = input("What will you do? ")
            
            if action == "1":
                # Use the character's attack method
                result = player.attack(monster)
                print(result)
                
            elif action == "2":
                # Cast spell
                if not player.known_spells:
                    print("You don't know any spells!")
                    continue
                    
                print("Available spells:")
                for i, spell in enumerate(player.known_spells, 1):
                    print(f"{i}. {spell.name} (Damage: {spell.damage}, Mana cost: {spell.mana_cost})")
                
                spell_choice = input("Choose a spell to cast (or 0 to cancel): ")
                if spell_choice == "0":
                    continue
                    
                try:
                    spell_index = int(spell_choice) - 1
                    if 0 <= spell_index < len(player.known_spells):
                        spell = player.known_spells[spell_index]
                        result = player.cast_spell(spell.name, monster)
                        print(result)
                        print(f"{monster_type} health: {monster.health}")
                        print(f"Your mana: {player.mana}/{player.max_mana}")
                    else:
                        print("Invalid spell selection.")
                except ValueError:
                    print("Please enter a number.")
                
            elif action == "3":
                # Use item
                if not player.inventory:
                    print("Your inventory is empty!")
                    continue
                    
                print("Your inventory:")
                for i, item in enumerate(player.inventory, 1):
                    print(f"{i}. {item}")
                
                item_choice = input("Choose an item to use (or 0 to cancel): ")
                if item_choice == "0":
                    continue
                    
                try:
                    item_index = int(item_choice) - 1
                    if 0 <= item_index < len(player.inventory):
                        item = player.inventory[item_index]
                        result = item.use(player)
                        print(result)
                        # Remove potion after use
                        if hasattr(item, 'effect_type'):
                            player.inventory.pop(item_index)
                    else:
                        print("Invalid item selection.")
                except ValueError:
                    print("Please enter a number.")
                
            elif action == "4":
                # Run away
                if random.random() < 0.5:  # 50% chance to escape
                    print("You managed to escape!")
                    return
                else:
                    print("You couldn't escape!")
            
            else:
                print("Invalid choice, turn lost!")
            
            # Monster turn (if still alive)
            if monster.health > 0:
                print("\nMonster's turn!")
                monster.attack(player, monster_attack)
                print(player)
                
                if not player.is_alive():
                    return
        
        # Combat ended
        if monster.health <= 0:
            print(f"You defeated the {monster_type}!")
            
            # Get rewards
            gold_reward = random.randint(5, 10) * player.level
            player.gold += gold_reward
            print(f"You found {gold_reward} gold!")
            
            # Random chance for item drop
            if random.random() < 0.3:  # 30% chance
                if random.random() < 0.7:  # 70% chance for potion vs weapon
                    potion = Potion("Health Potion", "Restores health", 20, "heal", 25)
                    player.inventory.append(potion)
                    print(f"You found a {potion.name}!")
                else:
                    weapon_damage = 10 + player.level * 2
                    found_weapon = Weapon("Better Sword", "A nicer sword", 30, weapon_damage)
                    player.inventory.append(found_weapon)
                    print(f"You found a {found_weapon.name}!")
            
            # Level up chance
            if random.random() < 0.2:  # 20% chance to level up
                player.level += 1
                player.max_health += 10
                player.health = player.max_health
                player.max_mana += 5
                player.mana = player.max_mana
                print(f"You leveled up! You are now level {player.level}!")
                print(player)
    else:
        # No monster encounter
        print("You explore the area but find nothing of interest.")

def visit_shop(player):
    # Create shop
    shop = Shop("Adventurer's Emporium")
    
    # Add items to shop based on player level
    shop.add_item(Potion("Health Potion", "Restores health", 20, "heal", 25), 20)
    shop.add_item(Potion("Mana Potion", "Restores mana", 20, "mana", 25), 20)
    
    if player.level >= 2:
        shop.add_item(Weapon("Steel Sword", "A better sword", 50, 15), 50)
        shop.add_item(Potion("Greater Health Potion", "Restores more health", 40, "heal", 50), 40)
    
    if player.level >= 3:
        shop.add_item(Spell("Ice Blast", 20, mana_cost=15, effect="freeze"), 100)
        shop.add_item(Weapon("Magic Staff", "A magical staff", 80, 20), 80)
    
    # Shopping loop
    shopping = True
    while shopping:
        print(f"\nWelcome to the {shop.name}! You have {player.gold} gold.")
        shop.display_items()
        
        print("\nWhat would you like to do?")
        print("1. Buy an item")
        print("2. Leave shop")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            item_index = input("Enter the number of the item you want to buy (or 0 to cancel): ")
            if item_index == "0":
                continue
                
            try:
                item_index = int(item_index)
                result = shop.buy(player, item_index)
                print(result)
            except ValueError:
                print("Please enter a number.")
                
        elif choice == "2":
            print("Thank you for visiting!")
            shopping = False
        else:
            print("Invalid choice, please try again.")

def check_inventory(player):
    print("\n=== YOUR INVENTORY ===")
    if player.equipped_weapon:
        print(f"Equipped weapon: {player.equipped_weapon}")
    else:
        print("No weapon equipped")
        
    if not player.inventory:
        print("Your inventory is empty!")
    else:
        print("\nItems:")
        for i, item in enumerate(player.inventory, 1):
            print(f"{i}. {item}")
            
    print(f"\nGold: {player.gold}")
    
    # Allow using items from inventory
    if player.inventory:
        use_item = input("\nWould you like to use an item? (y/n): ")
        if use_item.lower() == 'y':
            item_index = input("Enter the number of the item to use (or 0 to cancel): ")
            if item_index == "0":
                return
                
            try:
                item_index = int(item_index) - 1
                if 0 <= item_index < len(player.inventory):
                    item = player.inventory[item_index]
                    result = item.use(player)
                    print(result)
                    # Remove potion after use
                    if hasattr(item, 'effect_type'):
                        player.inventory.pop(item_index)
                else:
                    print("Invalid item selection.")
            except ValueError:
                print("Please enter a number.")

if __name__ == "__main__":
    main()