"""Tämä luokka luo esineet, joita pelissä käytetään."""
class Items:
    """Luokka esineille"""
    def __init__(self, name, description, effect, locations):
        self.name = name
        self.description = description
        self.effect = effect
        self.locations = locations
    def item_decoder(self, file):
        "Annetun tiedoston avulla palauttaa listan, joka sisältää item-olioita"
        itemlist = []
        for i in file:
            location_list = []
            i = i.replace("\n", "")
            split_i = i.split(";")
            locations = split_i[3]
            locations_split = locations.split(".")
            for j in locations_split:
                j_split = j.split(",")
                location_list.append((int(j_split[0]), int(j_split[1])))

            item = Items(split_i[0], split_i[1], split_i[2], location_list)
            itemlist.append(item)
        return itemlist
    def __str__(self):
        """Palauta kuvaus item-oliosta"""
        return f"{self.name},{self.description},{self.effect},{self.locations}"
