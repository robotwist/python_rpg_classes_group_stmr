class Item:
    """Base class for all items in the game."""
    
    def __init__(self, name, description, value):
        """Init item.
        
        Args:
            name (str): The item's name
            description (str): The item's description
            value (int): The item's gold value
        """
        self.name = name
        self.description = description
        self.value = value
    
    def use(self, character):
        """Use the item on a character.
        
        Args:
            character: The character using the item
            
        Returns:
            str: Result of using the item
        """
        return f"{character.name} can't use {self.name}."
    
    def __str__(self):
        """Return a string representation of the item."""
        return f"{self.name} ({self.value} gold) - {self.description}"


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


class Potion(Item):
    """A consumable potion that can restore health or provide other effects."""
    
    def __init__(self, name, description, value, effect_type, effect_value):
        """Initialize a potion.
        
        Args:
            name (str): The potion's name
            description (str): The potion's description
            value (int): The potion's gold value
            effect_type (str): The type of effect (e.g., "heal", "strength")
            effect_value (int): The magnitude of the effect
        """
        super().__init__(name, description, value)
        self.effect_type = effect_type
        self.effect_value = effect_value
    
    def use(self, character):
        """Apply the potion's effect to a character.
        
        Args:
            character: The character using the potion
            
        Returns:
            str: Result of using the potion
        """
        if self.effect_type == "heal":
            return character.heal(self.effect_value)
        # Could add other effect types here (strength boost, etc.)
        return f"{character.name} uses {self.name}, but nothing happens."
    
    def __str__(self):
        """Return a string representation of the potion."""
        return f"{self.name} ({self.value} gold) - {self.effect_type.capitalize()}: {self.effect_value} - {self.description}" 