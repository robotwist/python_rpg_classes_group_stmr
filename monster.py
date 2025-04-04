class Monster:
    def __init__(self, monster_type, health):
        self.monster_type = monster_type
        self.health = health
        self.loot = None  # Loot will be assigned later

    def attack(self, target, attack):
        """Perform an attack on a target."""
        if isinstance(target, Monster):
            target.health -= attack.damage
            print(f"{self.monster_type} attacked {target.monster_type} with {attack.name} for {attack.damage} damage!")
            if attack.special_effect:
                print(f"Special effect: {attack.special_effect}")
            if target.health <= 0:
                print(f"{target.monster_type} has been defeated!")
        else:
            print("Target must be a Monster!")

    def __str__(self):
        return f"{self.monster_type} with {self.health} health."

class Loot:
    def __init__(self, gold=0, weapon=None, potion=None):
        self.gold = gold
        self.weapon = weapon
        self.potion = potion

    def __str__(self):
        return f"Loot: {self.gold} gold, Weapon: {self.weapon}, Potion: {self.potion}"

class Attack:
    def __init__(self, name, damage, special_effect=None):
        self.name = name
        self.damage = damage
        self.special_effect = special_effect

    def __str__(self):
        return f"Attack: {self.name}, Damage: {self.damage}, Special Effect: {self.special_effect}"

# Example usage:
fireball = Attack("Moltov Cocktail", 30, "Burns the target")
slash = Attack("Slash", 15)


MelonTusk = Monster("MelonTusk", 100)
Drumpf = Monster("Drumpf", 50)

# Assign loot to the Drumpf monster
Drumpf.loot = Loot(gold=10, weapon="executive order", potion="tax fraud potion")

print(MelonTusk)  # Output: MelonTusk with 100 health.
print(Drumpf)  # Output: Drumpf with 50 health.

# MelonTusk attacks Drumpf
MelonTusk.attack(Drumpf, fireball)  # Output: Dragon attacked Goblin with Fireball for 30 damage!
                                 #         Special effect: Burns the target
print(Drumpf)  # Output: Drumpf with 20 health.

# Drumpf attacks MelonTusk
Drumpf.attack(MelonTusk, slash)  # Output: Drumpf attacked MelonTusk with Slash for 15 damage!
print(MelonTusk)  # Output: MelonTusk with 85 health.

# Print Drumpf's loot
print(Drumpf.loot)  # Output: Loot: 10 gold, Weapon: Dagger, Potion: Health Potion