class Monster:
    def __init__(self, monster_type, health):
        self.monster_type = monster_type
        self.health = health
        self.loot = None  # Loot will be assigned later

    def attack(self, target, attack):
        """Perform an attack on a target."""
        if hasattr(target, 'health'):
            # Calculate damage
            damage = attack.damage
            
            # Apply damage based on target type
            if hasattr(target, 'take_damage'):  # Character object
                result = target.take_damage(damage)
                print(result)
            else:  # Monster object
                target.health -= damage
                print(f"{self.monster_type} attacked {target.monster_type} with {attack.name} for {damage} damage!")
                if target.health <= 0:
                    print(f"{target.monster_type} has been defeated!")
            
            # Handle special effects
            if attack.special_effect:
                print(f"Special effect: {attack.special_effect}")
        else:
            print("Target must have a health attribute!")

    def __str__(self):
        return f"{self.monster_type} with {self.health} health."

class Loot:
    def __init__(self, gold=0, weapon=None, potion=None):
        """Initialize loot with gold and optional items.
        
        Args:
            gold (int): Amount of gold
            weapon (Weapon): A weapon item from the item module
            potion (Potion): A potion item from the item module
        """
        self.gold = gold
        self.weapon = weapon
        self.potion = potion

    def __str__(self):
        weapon_name = self.weapon.name if self.weapon else "None"
        potion_name = self.potion.name if self.potion else "None"
        return f"Loot: {self.gold} gold, Weapon: {weapon_name}, Potion: {potion_name}"

class Attack:
    def __init__(self, name, damage, special_effect=None):
        self.name = name
        self.damage = damage
        self.special_effect = special_effect

    def __str__(self):
        return f"Attack: {self.name}, Damage: {self.damage}, Special Effect: {self.special_effect}"

# Example usage:
if __name__ == "__main__":
    fireball = Attack("Moltov Cocktail", 30, "Burns the target")
    slash = Attack("Slash", 15)

    MelonTusk = Monster("MelonTusk", 100)
    Drumpf = Monster("Drumpf", 50)

    # Import the necessary classes to create proper loot
    from item import Weapon, Potion
    
    # Create weapon and potion objects
    executive_order = Weapon("Executive Order", "A powerful decree", 50, 25)
    tax_potion = Potion("Tax Fraud Potion", "Reduces your tax burden", 100, "heal", 20)
    
    # Assign loot to the Drumpf monster
    Drumpf.loot = Loot(gold=10, weapon=executive_order, potion=tax_potion)

    print(MelonTusk)  # Output: MelonTusk with 100 health.
    print(Drumpf)  # Output: Drumpf with 50 health.

    # MelonTusk attacks Drumpf
    MelonTusk.attack(Drumpf, fireball)
    print(Drumpf)

    # Drumpf attacks MelonTusk
    Drumpf.attack(MelonTusk, slash)
    print(MelonTusk)

    # Print Drumpf's loot
    print(Drumpf.loot)