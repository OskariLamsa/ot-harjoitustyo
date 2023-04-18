"""Tämä luokka 'huoneet' joita pelissä käytetään."""
print("hoi")
class Rooms:
    """Luokka huoneille"""
    def __init__(self, pysty, vaaka, name, description, item):
        self.pysty = int(pysty)
        self.vaaka = int(vaaka)
        self.name = name
        self.description = description
        self.item = item
    def room_decoder(self, tiedosto):
        "Annetun tiedoston avulla palauttaa listan, joka sisältää room-olioita."
        roomlist = []
        for i in tiedosto:
            i = i.replace("\n", "")
            split_i = i.split(";")
            room = Rooms(split_i[0], split_i[1], split_i[2], split_i[3], split_i[4])
            roomlist.append(room)
        return roomlist
    def __str__(self):
        """Palauta kuvaus room-oliosta."""
        return f"{self.pysty},{self.vaaka},{self.name},{self.description},{self.item}"
