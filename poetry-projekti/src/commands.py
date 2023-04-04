class Commands:
    def __init__():
        pass
    def command_handler(command):
        #Tämä funktio ottaa vastaan syotteen, paloittelee sen ja lähettää sen oikealle komennolle.
        command  = command.split(" ")
        if command[0] == "move":
           return Commands.move(command[1])
    def move(direction):
        #tee tähän chekki siitä, onko liike mahdollinen.
        if direction == "north":
            return "This is where you would move north!"
        elif direction == "east":
            return "This is where you would move east!"
        elif direction == "south":
            return "This is where you would move south!"
        elif direction == "west":
            return "This is where you would move west!"
        else:
            return "That is not a valid direction :("
