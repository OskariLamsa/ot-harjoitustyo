"""Tämä luokka luo 'viholliset' pelin käyttoon"""
class Enemies:
    def __init__(self, name, description, health, damage, hit_chance):
        self.name = name
        self.description = description
        self.health = int(health)
        self.damage = int(damage)
        self.hit_chance = int(hit_chance)
    def enemy_decoder(self, file):
        """Annetun tiedoston avulla palauttaa listan, joka sisältää enemy-olioita"""
        enemylist = []
        first = 1
        for k in file:
            if first == 1:
                first = 0
            else:
                k = k.replace("\n", "")
                split_e = k.split(";")
                enemy = Enemies(split_e[0], split_e[1], split_e[2], split_e[3], split_e[4])
                enemylist.append(enemy)
        return enemylist
    def __str__(self):
        """Palauta kuvaus item-oliosta"""
        return f"{self.name},{self.description},{self.health},{self.damage, self.hit_chance}"
