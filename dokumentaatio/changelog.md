## Viikko 3

Game.py on luotu, jossa on alkukantainen peliloop käynnissä, jossa voi syottaa tekstiä
commands.py on luotu, jossa on komentojen tulevaa logiikkaa esitelty
test1 testaa, että commands.py toimii oikein

## viikko 4
Rooms.py on luotu, jossa luodaan lista "room" olioita peliä varten. Tiedot luetaan "rooms.csv" tiedostosta. Tiedostoa muuttamalla voisi siis tehdä eri tasoja pelattavaksi.
Lisäksi peli nyt tietää pelaajan sijainnin, ja muuttaa sitä oikein "move" komennolla, mikäli kerrotussa ilmansuunnassa on huone.
Look-komento antaa huoneen deskription.
(Tällä hetkellä on vain aloitushuone, ja toinen huone suunnassa south. Näiden välillä voi liikkua kirjoittamalla move south ja move north)

## viikko 5
Items.py on luotu. Toimii samalla logiikalla kuin Rooms.py. Komentoja esineiden etsimiseen, käyttämiseen, ja listaamiseen. (search, use {item}, items).
Huoneet voivat olla nyt lukossa, kuten huone Bathroom todistaa. (south, south, west, west)
Esineiden käyttäminen ei vielä tee mitään erityistä. Lisäksi search-komennon avulla voi saada rajattoman määrän esinettä, sillä se ei poistu huoneesta.
Testit toimivat taas.
Repositorion rakenne siivottu.

## viikko 6
enemies.py on luotu. Logiikka on tuttu. Pelissä voi nyt joutua taisteluun. Peli valitsee sattumanvaraisest vihollisen taistelun alussa, ja taistelu kestää kunnes pelaaja päihittää
vihollisen tai pakenee (move komento, 50% mahdollisuus). Teksti nyt näkyy oiken pygame-ikkunan sisällä. Esineet key ja potion toimivat nyt, ja kun esine noukitaan huoneesta,
huoneessa ei ole enää esineitä. Io.py on myos luotu, joka vastaa tekstistä näytollä. Peli tallentuu nyt kun pelaaja poistuu pelistä. (Tallentaa vain pelaajan elämäpisteet ja sijainnin.
Tällä hetkellä huoneiden esineet tulevat takaisin, kun pelaaja poistuu pelistä ja tulee takaisin.)

## viikko 7
Huoneet nyt tallennetaan, jotta esineet eivät tule takaisin, kun pelaaja poistuu pelistä. Resources kansio luotu csv tiedostoille.
uusi komento buy antaa pelaajan ostaa esineitä. Lisää huoneita. Pelin voi nyt voittaa ja hävitä.
