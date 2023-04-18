"""Moduuli, joka prosessoi käyttäjän syotteen."""

class Commands:
    """Commands."""
    def __init__(self, game):
        self.game = game
        print(game.position)
    def command_handler(self ,command):
        """Tämä funktio ottaa vastaan syotteen, paloittelee sen ja vie sen oikealle komennolle."""
        command2 = command.split(" ")
        if command2[0] == "move":
            try:
                return Commands.move(self, command2[1])
            except IndexError:
                return "That is not a valid direction >:("
        if command == "look":
            return Commands.get_room(self, self.position[0], self.position[1]).description
        return "Check your commands, sir."
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
        tarkista_vaaka = direction[0]+self.position[0]
        tarkista_pysty = direction[1]+self.position[1]
        huone = Commands.get_room(self, tarkista_vaaka, tarkista_pysty)
        if huone is not None:
            self.position = (tarkista_vaaka, tarkista_pysty)
            return huone.description
        return "There is nothing there."

    def get_room(self, tarkista_pysty, tarkista_vaaka):
        """Palauttaa huoneen kordinaattien perusteella."""
        for i in self.rooms:
            if tarkista_pysty == i.pysty and tarkista_vaaka == i.vaaka:
                return i
        return None
