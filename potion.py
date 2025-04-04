from item import Item

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
        elif self.effect_type == "mana":
            original_mana = character.mana
            character.mana = min(character.max_mana, character.mana + self.effect_value)
            actual_restore = character.mana - original_mana
            return f"{character.name} restores {actual_restore} mana. Mana is now {character.mana}/{character.max_mana}"
        # Could add other effect types here (strength boost, etc.)
        return f"{character.name} uses {self.name}, but nothing happens."
    
    def __str__(self):
        """Return a string representation of the potion."""
        return f"{self.name} ({self.value} gold) - {self.effect_type.capitalize()}: {self.effect_value} - {self.description}"

# Example usage if this script is run directly
if __name__ == "__main__":
    # Create some potions
    health_potion = Potion("Health Potion", "Restores health", 50, "heal", 20)
    mana_potion = Potion("Mana Potion", "Restores mana", 60, "mana", 30)
    strength_potion = Potion("Strength Potion", "Increases strength temporarily", 75, "strength", 5)
    
    # Import Character for demonstration
    from character import Character
    
    # Create a character
    hero = Character("Hero", 100)
    
    # Character takes damage
    hero.take_damage(30)
    print(hero)  # Should show reduced health
    
    # Use healing potion
    result = health_potion.use(hero)
    print(result)
    print(hero)  # Should show increased health
    
    # Use mana potion
    hero.mana -= 20  # Reduce mana for demonstration
    print(f"Mana reduced to {hero.mana}/{hero.max_mana} for demonstration")
    result = mana_potion.use(hero)
    print(result)
    
    # Use strength potion (currently has no effect as it's not implemented)
    result = strength_potion.use(hero)
    print(result)






