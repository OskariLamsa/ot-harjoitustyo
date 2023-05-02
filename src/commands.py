"""Moduuli, joka prosessoi käyttäjän syotteen."""
#pylint: disable=no-member
#Yllä oleva ajaa saman asian kuin whitelistaaminen, joka ei toiminut.
from random import randint
class Commands:
    """Commands."""
    def __init__(self, game):
        self.game = game
        self.position = game.position
        self.in_combat = game.in_combat
    def command_handler(self ,command):
        """Tämä funktio ottaa vastaan syotteen, paloittelee sen ja vie sen oikealle komennolle."""
        command2 = command.split(" ")
        if len(command2) == 2:
            return Commands.split_command_handler(self, command2[0], command2[1])
        if command == "look":
            room = Commands.get_room(self, self.position[0], self.position[1]).description
            return room + "\n" + f"{self.find_adjacent_rooms()}"
        if command == "attack":
            return Commands.player_attack(self)
        if command == "items":
            return Commands.get_items(self)
        if command == "search":
            item = Commands.get_item_by_location(self, self.position[0], self.position[1])
            if not isinstance(item, str)  and item is not None:
                self.player_items.append(item)
                to_return = "You have found a " +f"{item.name}."
            else:
                to_return = "You unfortunately found nothing."
            return to_return
        return "Check your commands, sir."
    def split_command_handler(self, first, second):
        if first == "move":
            return Commands.move(self, second)
        if first == "use":
            return Commands.item_check(self, second)

        return "Check your commands, sir."
    def get_item_by_location(self, horizontal, vertical):
        """Palauta item-olio huoneen kordinaatien perusteella. Poista item huoneesta."""
        for i in self.rooms:
            if i.horizontal == horizontal and i.vertical == vertical and i.item != "none":
                to_return = i.item
                i.item = str("none")
                return to_return
        return None
    def get_item_by_name(self, item_name):
        """Palauta item-olio nimen perusteella."""
        for i in self.items:
            if i.name == item_name:
                return i
        return None
    def use_item(self, item):
        """Jokaiselle itemille on oma funktio."""
        split_effect = item.effect.split(" ")
        if item.name == "key":
            return Commands.use_key(self)
        if split_effect[0] == "heal":
            return Commands.use_heal_item(self, int(split_effect[1]))
        return "This item can't be used."
    def use_key(self):
        """Etsi lukittuja ovia lähettyviltä, ja avaa ensimmäinen, joka loytyy."""
        for i in self.rooms:
            if self.position[0]-1==i.horizontal and self.position[1]==i.vertical and i.locked==1:
                i.locked = 0
                return f"You used the key to unlock the {i.name}"
            if self.position[0]+1==i.horizontal and self.position[1]==i.vertical and i.locked==1:
                i.locked = 0
                return f"You used the key to unlock the {i.name}"
            if self.position[0]==i.horizontal and self.position[1]-1==i.vertical and i.locked==1:
                i.locked = 0
                return f"You used the key to unlock the {i.name}"
            if self.position[0]==i.horizontal and self.position[1]+1==i.vertical and i.locked==1:
                i.locked = 0
                return f"You used the key to unlock the {i.name}"
        return "Nothing to unlock here."
    def use_heal_item(self, heal):
        """Tämä funktio parantaa pelaajaa tietyn määrän

        Args:
            heal (int): Nosta pelaajan elämäpisteitä tällä numerolla

        Returns:
            str: Kertoo, että olet saanut elämäpisteitä
        """
        self.health += int(heal)
        return f"You have healed for {heal} health!"
    def item_check(self, item_name):
        """Tarkista, onko kyseinen item pelaajalla."""
        for i in self.player_items:
            if i.name == item_name:
                return Commands.use_item(self, i)
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
        Jos voi, palauttaa huoneen description ja liikuttaa pelaajaa.
        Jos pelaaja on taistelussa, hänellä on 50% mahdollisuus päästä karkuun.
        Jos tämä ei onnistu, häntä lyodään.
        Aina kun pelaaja liikkuu huoneesta toiseen, nousee taistelun mahdollisuudet 10%.
        """
        check_vertical = direction[0]+self.position[0]
        check_horizontal = direction[1]+self.position[1]
        room = Commands.get_room(self, check_vertical, check_horizontal)
        if room is not None:
            if room.locked == 1:
                to_return = "That room is locked!"
            if self.in_combat == 1:
                if randint(0,1) == 1:
                    return "But you couldn't get away!" + "\n" + Commands.enemy_attack(self,
                     self.enemy.name)
                self.in_combat = 0
                return ("You managed to flee!" + "\n" +
                        room.description +"\n" + f"{self.find_adjacent_rooms()}")
            combat_calculation = randint(0, 100)
            if combat_calculation <= self.combat_chance:
                return room.description + "\n" + Commands.combat_start(self)
            self.combat_chance += 10
            print(f"chance is now {self.combat_chance}")
            self.position = (check_vertical, check_horizontal)
            to_return = room.description + "\n" + f"{self.find_adjacent_rooms()}"
        else:
            to_return = "There is nothing there."
        return to_return
    def combat_start(self):
        """Tekee tarvittavat toimenpiteet taistelun alussa. Asettaa pelin in_combat moodiin,
        nollaa taistelun mahdollisuuden, ja valitsee sattumanvaraisesti vihollisen.

        Returns:
            str: Kertoo pelaajalle, mikä vihollinen käy päälle.
        """
        self.in_combat = 1
        self.combat_chance = 0
        self.enemy = self.enemies[randint(0, len(self.enemies)-1)]
        return f"You have been ambushed by a {self.enemy.name}!"
    def enemy_attack(self, enemy_name):
        """Vihollinen hyokkää pelaajaan. Tämä voi aiheuttaa elämäpisteiden vähentymistä.

        Args:
            enemy_name (str): vihollisen nimi

        Returns:
            str: Kertoo pelaajalle, osuuko vai ei osu
        """
        for i in self.enemies:
            if i.name == enemy_name:
                if randint(0, 100) < i.hit_chance:
                    self.health -= i.damage
                    return f"The {i.name} hits you for {i.damage} damage!"
                return f"The {i.name} attacks you, but misses!"
        return None
    def player_attack(self):
        """Pelaajan hyokkäys. Tämä voi vähentää vihollisen elämäpisteitä. Jos ne putoavat
        nollaan tai alle, vihollinen päihitetään.

        Returns:
            str: Kertoo pelaajalle, osuuko vai ei osu
        """
        if self.in_combat == 0:
            return "There are no enemies to attack."
        if randint(0, 100) < self.enemy.hit_chance:
            self.enemy.health -= 3
            if self.enemy.health <= 0:
                self.in_combat = 0
                return f"You hit and defeat the {self.enemy.name}"
            return (f"You hit the {self.enemy.name}" + "\n" +
            Commands.enemy_attack(self, self.enemy.name))
        return "You miss." + "\n" + Commands.enemy_attack(self, self.enemy.name)
    def get_room(self, check_horizontal, check_vertical):
        """Palauttaa huoneen kordinaattien perusteella."""
        for i in self.rooms:
            if check_horizontal == i.horizontal and check_vertical == i.vertical:
                return i
        return None
