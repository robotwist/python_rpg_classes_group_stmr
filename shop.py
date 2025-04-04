from item import Item
from weapon import Weapon
from potion import Potion
from spell import Spell

class Shop:
    """A shop that allows players to buy magical items like potions and spells."""
    def __init__(self, name="Magic Shop", inventory=None):
        """Initialize a shop with an inventory of items.
        
        Args:
            name (str): The name of the shop
            inventory (list): A list of items available for sale
        """
        self.name = name
        self.inventory = inventory or []  # List of items (Potion, Spell, etc.)
    
    def add_item(self, item, price=None):
        """Add an item to the shop inventory.
        
        Args:
            item: The item to add (Weapon, Potion, Spell, etc.)
            price (int, optional): Override the default price
        """
        if price is not None:
            item.shop_price = price
        else:
            # Default price if not specified
            item.shop_price = getattr(item, 'value', 10)
        
        self.inventory.append(item)
    
    def display_items(self):
        """Display all items available for purchase."""
        print(f"Welcome to {self.name}!")
        if not self.inventory:
            print("Sorry, we're out of stock!")
            return
            
        for i, item in enumerate(self.inventory, 1):
            price = getattr(item, 'shop_price', 10)
            print(f"{i}. {item} - {price} gold")
    
    def buy(self, player, item_index):
        """Allow a player to buy an item.
        
        Args:
            player: The character buying the item
            item_index (int): The index of the item to buy
            
        Returns:
            str: Result of the purchase
        """
        if not hasattr(player, 'gold'):
            return f"{player.name} doesn't have a gold pouch!"
        
        if not hasattr(player, 'inventory'):
            return f"{player.name} doesn't have an inventory to store items!"
            
        if 0 < item_index <= len(self.inventory):
            item = self.inventory[item_index - 1]
            item_cost = getattr(item, 'shop_price', 10)
            
            if player.gold >= item_cost:
                player.gold -= item_cost
                player.inventory.append(item)
                return f"{player.name} bought {item.name} for {item_cost} gold!"
            else:
                return f"{player.name} doesn't have enough gold! Need {item_cost} gold."
        else:
            return "Invalid item selection."
    
    def __str__(self):
        """Return a string representation of the shop."""
        return f"{self.name} - A quaint little shop filled with mystical items ({len(self.inventory)} items in stock)"

# Example usage if this script is run directly
if __name__ == "__main__":
    # Create a shop
    magic_shop = Shop("Ollivander's Magical Emporium")
    
    # Create some items to sell
    health_potion = Potion("Health Potion", "Restores health", 50, "heal", 20)
    mana_potion = Potion("Mana Potion", "Restores mana", 60, "mana", 30)
    sword = Weapon("Steel Sword", "A sharp blade", 100, 25)
    fireball = Spell("Fireball", 30, mana_cost=15, effect="burn")
    
    # Add items to the shop
    magic_shop.add_item(health_potion)
    magic_shop.add_item(mana_potion, 75)  # Override price
    magic_shop.add_item(sword)
    magic_shop.add_item(fireball, 200)  # Spells are expensive!
    
    # Display the shop's inventory
    magic_shop.display_items()
    
    # Create a player with gold and inventory
    from character import Character
    player = Character("Adventurer", 100)
    player.gold = 300  # Add gold attribute
    player.inventory = []  # Add inventory attribute
    
    # Buy an item
    result = magic_shop.buy(player, 1)  # Buy the health potion
    print(result)
    
    # Show remaining gold
    print(f"{player.name} has {player.gold} gold remaining.")
    
    # Try to buy an expensive item
    result = magic_shop.buy(player, 4)  # Try to buy the fireball spell
    print(result) 