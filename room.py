# Define the Room class.

class Room:
    """
    This class represents a room. It is composed by its name, description and its possible exits.

    Attributes:
        name (str): The name of the room.
        descrition (str): The description of what the room contains/looks like.
        exits (dict): The different possible exits that the player can take in the form of key = direction (str) and value=room (room)
    
    Methods:
        __init__(self, name, description): The constructor
        get_exit(self, direction): The room in a given direction if it exists
        get_exit_string(self): The string used in the next function to tell the player his possibilities (exits)
        get_long_description(self): Actually builds the string telling the player in which room he is with a descriptipn and what are his possible exits
    Examples:

    >>> forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
    >>> tower = Room("Tower", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
    >>> cave = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
    >>> cottage = Room("Cottage", "dans un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
    >>> swamp = Room("Swamp", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
    >>> castle = Room("Castle", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
    >>> forest.exits = {"N" : cave, "E" : tower, "S" : castle, "O" : None}
    >>> tower.exits = {"N" : cottage, "E" : None, "S" : swamp, "O" : forest}
    >>> cave.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None}
    >>> cottage.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave}
    >>> swamp.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle}
    >>> castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None}
    >>> tower.get_exit(N)
    cottage
    >>> tower.get_exit(E)
    None
    >>> tower.get_long_description()
    Vous êtes dans une immense tour en pierre qui s'élève au dessus des nuages.

    Sorties: N, S, O
    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
