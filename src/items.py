"""Tämä luokka luo esineet, joita pelissä käytetään."""
class Items:
    """Luokka esineille"""
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect
    def item_decoder(self, file):
        """Palauta lista item-olioita. Jättää ekan linen tiedostossa huomiotta,
        sillä se sisältää kuvauksen.

        Args:
            file (csv): items.csv

        Returns:
            list: items[]
        """
        itemlist = []
        first = 1
        for i in file:
            if first == 1:
                first = 0
            else:
                i = i.replace("\n", "")
                split_i = i.split(";")
                item = Items(split_i[0], split_i[1], split_i[2])
                itemlist.append(item)
        return itemlist
    def __str__(self):
        """Palauta kuvaus item-oliosta"""
        return f"{self.name},{self.description},{self.effect}"
