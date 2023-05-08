```mermaid
classDiagram
class Game{
 +list rooms
 +tuple position
 +start()
 }
 class Rooms{
 +int pysty
 +int vaaka
 +str name
 +str description
 +str item
 +room_decoder()
 }
class Commands{
 +command_handler()
 +move()
 +move_checker()
 +get_room()
 }
Game --> Rooms
Game --> Commands
Game.py alustetaan niin, että se kutsuu items-luokkaa, ja antaa sille items.csv tiedoston. items-luokka palauttaa item-olioita.
Seuraavaksi Game kutsuu rooms-luokkaa, antaen sille listan items-olioita, ja rooms.csv tiedoston. Rooms luo listan käyttäen joko annettua tiedostoa, tai tallennustiedostoa, jos sellainen on. rooms palauttaa gamelle listan room-olioita.
Games yrittää käyttää save.csv tiedstoa, jos sellainen on. start() funktio aloittaa pelin, ja jatkaa niin kauan kunnes events() palauttaa False. Events tarkistaa onko pelaaja kuollut.
Jos ei, niin input_textiin lisätään pelaajan antama syote. Kun pelaaja painaa enter painiketta, kutsutaan input_entry().
input_entry() kutsuu Commands.command_handler, jolle annetaan pelaajan syote. Commands prosessoi pelaajan syotteen, sen seurakset, ja palauttaa tekstiä. Tämä teksti lisätään IO.text tekstiin, kuten myos pelaajan antama syote.
IO.text sisältää siis kaiken tekstin, mitä pelaaja pelissä näkee, lukuunottamatta Health, Money ja Combat tekstiä.
Pelaajan input.text nollataan, ja IO.update_screen() kutsutaan. Tämä piirtää tekstit näytolle.
Sitten kun pelaaja sulkee pelin, peli kutsuu save() funktiota, joka tallentaa edistyksen kahteen tiedostoon: save.csv ja rooms_save.csv. Huoneisiin siis tallennetaan tieto siitä, onko esine otettu, tai huone avattu avaimella.
