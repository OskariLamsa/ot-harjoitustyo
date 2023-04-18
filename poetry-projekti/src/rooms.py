"""Tämä tiedosto sisältää 'huoneet' joita pelissä käytetään"""
print("hoi")
class Rooms:
    """Luokka huoneille"""
    def __init__(self, x, y, name, description, item):
        self.x = x
        self.y = y
        self.name = name
        self.description = description
        self.item = item
    def RoomDecoder():
        f = open("rooms.csv", "r")
        roomlist = []
        for i in f:
            i = i.replace("\n", "")
            e = i.split(";")
            room = Rooms(e[0], e[1], e[2], e[3], e[4])
            roomlist.append(room)
        return roomlist
    def __str__(self):
        return(f"{self.x},{self.y},{self.name},{self.description},{self.item}")


