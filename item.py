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

# Example usage if this script is run directly
if __name__ == "__main__":
    # Create a basic item
    test_item = Item("Test Item", "This is a test item", 5)
    print(test_item) 