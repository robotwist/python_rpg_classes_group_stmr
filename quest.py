from weapon import Weapon
from potion import Potion
from loot import Loot
from monster import Monster

default_quests = [
    {
        "name": "Save the Kingdoms Treasury",
        "description": "Defeat the evil monarch and his handmaid to save the kingdom from financial ruin.",
        "rewards": {
            "experience": 100,
            "items": [Weapon("Sword of Justice", "sword", 1, 15),
                      Potion("Woke Mind Virus", heal, 1), 
                      Potion("Soros Sauce", heal, 1)],
            "gold": 50,
        "enemies": [
            Monster("MelonTusk", 100),
            Monster("Drumpf", 50),
            Monster("Rabid Doge", 5),
            Monster("Rabid Doge", 5),
            Monster("Rabid Doge", 5),
            Monster("Rabid Doge", 5),
            Monster("Rabid Doge", 5),
            Monster("Rabid Doge", 5),
            Monster("Rabid Doge", 5),
        ]
        }
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
                Weapon("Pen of Providence", "pen", 1, 10),
                Potion("Diplomacy Draught", heal, 1)
            ],
            "gold": 75,
        },
        "enemies": [
            Monster("Ronall McConnell", 120),
            Monster("Lady G", 80),
            Monster("Bull Shaman", 60),
            Monster("That One Uncle", 40),
            Monster("Your Uncles Buddy", 40),
        ]
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
                Weapon("Gavel of Justice", "mace", 1, 20),
                Potion("Oratory Elixir", heal, 1)
            ],
            "gold": 100,
        },
        "enemies": [
            Monster("Spin Doctor", 90),
            Monster("Obstruction Ogre", 110),
            Monster("Filibuster Frog", 50),
            Monster("Lobbying Leprechaun", 30),
            Monster("Lobbying Leprechaun", 30),
        ]
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
                Weapon("Order's Oath", "sword", 1, 25),
                Potion("Unity Brew", heal, 1)
            ],
            "gold": 150,
        },
        "enemies": [
            Monster("Tweeting Tempest", 100),
            Monster("Partisan Poltergeist", 75),
            Monster("Caucus Kraken", 130),
            Monster("Debate Demon", 90),
        ]
    },
]

class Quest:
    def __init__(self, name, description, rewards):
        self.name = name
        self.description = description
        self.rewards = { 
            experience = rewards.experience,
            items = rewards.items,
            gold = rewards.gold
        }
        self.is_completed = False
        self.is_available = True

    def __str__(self):
        return f"Quest: {self.name}\nDescription: {self.description}\nRewards: {self.rewards.experience} XP, {self.rewards.gold} gold, Items: {', '.join(self.rewards.items)}"
    
        
    def complete(self, player):
        print(f"{player.name} has completed the quest: {self.name}")
        player.add_experience(self.reward.experience)
        player.add_items(self.rewards.items)
        player.gold += self.rewards.gold
        self.is_completed = True
        self.is_available = False
        print(f"Congratulations {player.name}! You have completed the quest: {self.name}")
        print(f"you have been awarded {self.rewards.experience} experience points, and {self.rewards.gold} gold.")
        print(f"You have received: {', '.join(self.rewards.items)}")
        
    
        