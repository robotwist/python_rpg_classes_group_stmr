class Character:
    def __init__(self, name, health, level=1):
        self.name = name
        self.max_health = health
        self.health = health
        self.level = level

    def is_alive(self):
        """Check if still alive"""
        return self.health > 0
    
    def take_damage(self, damage):
        """Reduce Health by damage amount report result"""
        self.health -= max(0, self.health - damage)
        if self.health == 0:
            return f"{self.name} takes {damage} damage and falls to his own demise!"
        else:
            return f"{self.name} takes {damage} damage and is now at {self.health} health!"
    def heal(self, amount):
        """Heal the character by the given amount.
        
        Args:
            amount (int): The amount to heal
            
        Returns:
            str: Description of the healing done
        """
        self.health = min(self.max_health, self.health + amount)
        return f"{self.name} heals for {amount}. Health is now {self.health}"
    
    def __str__(self):
        """Return a string representation of the character."""
        return f"{self.name} (Lvl {self.level}) - HP: {self.health}/{self.max_health}" 