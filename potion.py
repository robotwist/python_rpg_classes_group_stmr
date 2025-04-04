from item import Potion, Item


# Example of creating and using potions:
if __name__ == "__main__":
    # Create some potions
    health_potion = Potion("Health Potion", "Restores health", 50, "heal", 20)
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
    
    # Use strength potion (currently has no effect as it's not implemented)
    result = strength_potion.use(hero)
    print(result)






