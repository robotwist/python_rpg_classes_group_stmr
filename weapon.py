from item import Item

class Weapon(Item):
    """A weapon that can be equipped and used in battle."""
    
    def __init__(self, name, description, value, damage):
        """Initialize a weapon.
        
        Args:
            name (str): The weapon's name
            description (str): The weapon's description
            value (int): The weapon's gold value
            damage (int): The weapon's base damage
        """
        super().__init__(name, description, value)
        self.damage = damage
    
    def use(self, character):
        """Equip the weapon if the character has an equip_weapon method.
        
        Args:
            character: The character equipping the weapon
            
        Returns:
            str: Result of equipping the weapon
        """
        if hasattr(character, 'equip_weapon'):
            return character.equip_weapon(self.name)
        return super().use(character)
    
    def __str__(self):
        """Return a string representation of the weapon."""
        return f"{self.name} ({self.value} gold) - Damage: {self.damage} - {self.description}"

# Example usage if this script is run directly
if __name__ == "__main__":
    # Create a weapon
    sword = Weapon("Steel Sword", "A sharp blade", 100, 25)
    print(sword)
    
    # Import Character for demonstration
    from character import Character
    
    # Create a character
    hero = Character("Hero", 100)
    
    # Use the weapon
    result = sword.use(hero)
    print(result)
    print(hero) 