"""Moduuli, joka prosessoi käyttäjän syotteen."""
#pylint: disable=no-member
#Yllä oleva ajaa saman asian kuin whitelistaaminen, joka ei toiminut.
class Commands:
    """Commands."""
    def __init__(self, game):
        self.game = game
        self.position = game.position
        self.items = game.items
    def command_handler(self ,command):
        """Tämä funktio ottaa vastaan syotteen, paloittelee sen ja vie sen oikealle komennolle."""
        command2 = command.split(" ")
        if len(command2) == 2:
            return Commands.split_command_handler(self, command2[0], command2[1])
        if command == "look":
            room = Commands.get_room(self, self.position[0], self.position[1]).description
            return room + "\n" + f"{self.find_adjacent_rooms()}"
        if command == "items":
            return Commands.get_items(self)
        if command == "search":
            item = Commands.get_item_by_location(self, self.position[0], self.position[1])
            if item is None:
                to_return = "You unfortunately found nothing."
            else:
                self.player_items.append(item)
                to_return = "You have found a " +f"{item.name}."
            return to_return
        return "Check your commands, sir."
    def split_command_handler(self, first, second):
        if first == "move":
            return Commands.move(self, second)
        if first == "use":
            return Commands.use_item(self, second)

        return "Check your commands, sir."
    def get_item_by_location(self, horizontal, vertical):
        """Palauta item-olio huoneen kordinaatien perusteella."""
        for i in self.items:
            for j in i.locations:
                if j[0] == horizontal and j[1] == vertical:
                    return i
        return None
    def get_item_by_name(self, item_name):
        """Palauta item-olio nimen perusteella."""
        for i in self.items:
            if i.name == item_name:
                return i
        return None
    def use_item(self, item_name):
        """Käytä esinettä. Tämä funktio on vielä kesken."""
        for i in self.player_items:
            if i.name == item_name:
                if Commands.get_item_by_name(self, item_name):
                    return f"You used the {item_name}."
        return "You don't have an item by that name."
    def get_items(self):
        """Listaa pelaajan esineet, tai kerro, ettei niitä ole."""
        if len(self.player_items) == 0:
            palaute = "You have no items.."
        else:
            palaute = "Your items are: "
            for i in self.player_items:
                palaute += i.name + ", "
        return palaute[0:-2] + "."

    def move(self, direction):
        """vie move-komento tarkistukseen."""

        if direction == "north":
            return Commands.move_checker(self, (-1,0))
        if direction == "east":
            return Commands.move_checker(self, (0,1))
        if direction == "south":
            return Commands.move_checker(self, (1,0))
        if direction == "west":
            return Commands.move_checker(self, (0,-1))
        return "That is not a valid direction :("
    def move_checker(self, direction):
        """Tarkistaa voiko huoneeseen liikkua.
        Jos voi, palauttaa huoneen description ja liikuttaa pelaajaa."""
        check_vertical = direction[0]+self.position[0]
        check_horizontal = direction[1]+self.position[1]
        room = Commands.get_room(self, check_vertical, check_horizontal)
        if room is not None:
            if room.locked == 1:
                palaute = "That room is locked!"
            else:
                self.position = (check_vertical, check_horizontal)
                palaute = room.description + "\n" + f"{self.find_adjacent_rooms()}"
        else:
            palaute = "There is nothing there."
        return palaute
    def get_room(self, check_horizontal, check_vertical):
        """Palauttaa huoneen kordinaattien perusteella."""
        for i in self.rooms:
            if check_horizontal == i.horizontal and check_vertical == i.vertical:
                return i
        return None
