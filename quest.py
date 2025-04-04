from weapon import Weapon
from potion import Potion
from item import Item
from monster import Monster

class Quest:
    def __init__(self, name, description, rewards, enemy):
        self.name = name
        self.description = description
        self.rewards = rewards
        self.enemy = enemy
        self.is_completed = False
        self.is_available = True

    
        
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
        
    
        