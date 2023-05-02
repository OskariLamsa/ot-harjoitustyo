"""Tämä luokka luo 'huoneet' joita pelissä käytetään."""
class Rooms:
    """Luokka huoneille"""
    def __init__(self, horizontal, vertical, name, description, locked, item):
        "Tässä erikoisuutena on se, että huoneet saavat item-olioita osakseen"
        self.horizontal = int(horizontal)
        self.vertical = int(vertical)
        self.name = name
        self.description = description
        self.locked = int(locked)
        self.item = item
    def room_decoder(self,file,items):
        """Palauta lista huone-olioita. Jättää ekan linen huomiotta,
        sillä se sisältää kuvauksen.

        Args:
            file (csv): rooms.csv
            items (list): self.items[]

        Returns:
            list: rooms[]
        """
        roomlist = []
        first = 1
        for j in file:
            if first == 1:
                first = 0
            else:
                j = j.replace("\n", "")
                split_j = j.split(";")
                item = ''
                for j in items:
                    if split_j[5] == j.name:
                        item = j
                room = Rooms(split_j[0], split_j[1], split_j[2], split_j[3], split_j[4], item)
                roomlist.append(room)
        return roomlist
    def __str__(self):
        """Palauta kuvaus room-oliosta."""
        return f"{self.horizontal},{self.vertical},{self.name},"\
            +f"{self.description},{self.locked},{self.item}"
