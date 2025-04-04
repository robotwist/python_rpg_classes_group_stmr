from character import Character
from monster import Monster, Attack, Loot
from item import Weapon, Potion

# Create a character
hero = Character("Sir Lancelot", 100, level=5)
print(f"Created hero: {hero}")

# Create some weapons
sword = Weapon("Excalibur", "A legendary sword", 500, 40)
dagger = Weapon("Dagger", "A small but quick weapon", 25, 10)

# Create some potions
health_potion = Potion("Health Potion", "Restores health", 50, "heal", 30)
strength_potion = Potion("Strength Potion", "Increases strength", 75, "strength", 5)

# Create some monsters
dragon = Monster("Dragon", 200)
goblin = Monster("Goblin", 30)

# Create some attacks
fire_breath = Attack("Fire Breath", 35, "Burns the target")
claw_attack = Attack("Claw Attack", 20)
punch = Attack("Punch", 5)

# Assign loot
dragon.loot = Loot(gold=100, weapon=sword, potion=health_potion)
goblin.loot = Loot(gold=10, weapon=dagger)

print("\n=== ADVENTURE BEGINS ===\n")

# Battle with the goblin
print(f"A {goblin.monster_type} appears!")
hero.equip_weapon(dagger.name)
print(f"{hero}")

# Monster attacks hero
print("\n--- Combat Round 1 ---")
goblin.attack(hero, claw_attack)
print(hero)

# Hero uses a potion
print("\n--- Using Items ---")
result = health_potion.use(hero)
print(result)
print(hero)

# Fight the dragon
print("\n=== BOSS BATTLE ===")
print(f"A fearsome {dragon.monster_type} appears!")

# Dragon attacks
print("\n--- Combat Round 1 ---")
dragon.attack(hero, fire_breath)
print(hero)

# Hero equips a better weapon
print("\n--- Equipping New Weapon ---")
result = sword.use(hero)  # Uses the weapon
print(result)
print(hero)

# Collect loot after defeating a monster
print("\n=== VICTORY ===")
print(f"You've defeated the monsters and collected loot!")
print(f"From the dragon: {dragon.loot}")
print(f"From the goblin: {goblin.loot}")

print("\n=== ADVENTURE COMPLETE ===") 