from character import Character
from weapon import Weapon
from quest import Quest
from potion import Potion
from item import Item
from monster import Monster
from battle import Battle

default_quests = [
    {
        "name": "Save the Kingdoms Treasury",
        "description": "Defeat the evil monarch and his handmaid to save the kingdom from financial ruin.",
        "rewards": {
            "experience": 100,
            "items": [Weapon("Sword of Justice", "sword", 100, 15),
                      Potion("Woke Mind Virus", "", 10, "heal", 50), 
                      Potion("Soros Sauce", "", 10, "heal", 25),
                      Item("Declaration of Independence", "A document that grants you freedom", 1000)
                     ],
            "gold": 50,
        },
        "enemy": Monster("MelonTusk", 100)
    },
    {
        "name": "Guard the Grand Capitol",
        "description": (
            "The sacred halls of government are under siege! The nefarious Lobbyist Lich and his minions of bureaucratic decay "
            "have infiltrated the Capitol. Rally your courage to purge these corrupt forces from the hallowed chambers of power."
        ),
        "rewards": {
            "experience": 150,
            "items": [
                Weapon("Pen of Providence", "dagger", 90, 10),
                Potion("Diplomacy Draught", "", 10, "heal", 25)
            ],
            "gold": 75,
        },
        "enemy": Monster("Ronall McConnell", 120)
    },
    {
        "name": "Seal the Senate Sessions",
        "description": (
            "Chaos reigns in the Senate chambers! A cadre of conniving Spin Doctors and obstructionist Ogres threatens to paralyze "
            "legislative proceedings. Restore order by dismantling their disruptive regime before governance crumbles into pandemonium."
        ),
        "rewards": {
            "experience": 200,
            "items": [
                Weapon("Gavel of Justice", "mace", 110, 20),
                Potion("Oratory Elixir", "", 10, "heal", 25)
            ],
            "gold": 100,
        },
        "enemy": Monster("Spin Doctor", 90)
    },
    {
        "name": "Restore the Executive's Command",
        "description": (
            "The executive branch teeters on the brink! Partisan Poltergeists and the dreaded Tweeting Tempest sow discord "
            "throughout the corridors of power. Stand as the bulwark of order and rally the nation's leadership back to glory."
        ),
        "rewards": {
            "experience": 250,
            "items": [
                Weapon("Order's Oath", "sword", 100, 25),
                Potion("Unity Brew", "", 10, "heal", 25)
            ],
            "gold": 150,
        },
        "enemy": Monster("Tweeting Tempest", 100)
    },
]

def setupQuests():
    quests = []
    for quest in default_quests:
        new_quest = Quest(
            name=quest["name"],
            description=quest["description"],
            rewards=quest["rewards"],
            enemy=quest["enemy"]
        )
        quests.append(new_quest)
    return quests

def main():
    character = {}
    
    print("Enter your heros name: ")
    character['name'] = input()
    print("Pick your weapon type (sword, mace, dagger): ")
    weapon_type = input()
    if weapon_type == "sword":
        character['weapon'] = "Sword"
    elif weapon_type == "mace":
        character['weapon'] = "Mace"
    elif weapon_type == "dagger":
        character['weapon'] = "Dagger"
    else:
        print("Invalid weapon type. Defaulting to Sword.")
        character['weapon'] = "Sword"
        
    hero = Character(character['name'], 100)
    weapon = Weapon(character['weapon'], "A mighty weapon", 100, 25)
    hero.equip_weapon(weapon.name)
    print(f"{hero.name} has equipped a {hero.equipped_weapon}.")
    quests = setupQuests()
    print("Choose a quest by number:")
    for i, quest in enumerate(quests):
        print(f"{i + 1}. {quest.name}")
    quest_choice = int(input()) - 1
    if 0 <= quest_choice < len(quests):
        selected_quest = quests[quest_choice]
        print(f"You have chosen the quest: {selected_quest.name}")
        print("")
        print(selected_quest.description)
        print("")
        print("Rewards:")
        print("----------------------")
        for reward in selected_quest.rewards['items']:
            print(reward)
        print("Gold:", selected_quest.rewards['gold'])
        print("Experience:", selected_quest.rewards['experience'])
        print("----------------------")
        print("Enemies:\n", selected_quest.enemy)
        print("----------------------")
    else:
        print("Invalid choice. No quest selected.")
        
    combat = Battle(hero, selected_quest.enemy)
    combat.start()
    
    
    print("Game Over")
    print("Thank you for playing!")
main()