"""Tämä luokka luo 'huoneet' joita pelissä käytetään."""
class Rooms:
    """Luokka huoneille"""
    def __init__(self, horizontal, vertical, name, description, locked):
        self.horizontal = int(horizontal)
        self.vertical = int(vertical)
        self.name = name
        self.description = description
        self.locked = int(locked)
    def room_decoder(self,file):
        "Annetun tiedoston avulla palauttaa listan, joka sisältää room-olioita."
        roomlist = []
        for i in file:
            i = i.replace("\n", "")
            split_i = i.split(";")
            room = Rooms(split_i[0], split_i[1], split_i[2], split_i[3], split_i[4])
            roomlist.append(room)
        return roomlist
    def __str__(self):
        """Palauta kuvaus room-oliosta."""
        return f"{self.horizontal},{self.vertical},{self.name},{self.description},{self.locked}"
