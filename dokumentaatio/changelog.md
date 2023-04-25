##Viikko 3

Game.py on luotu, jossa on alkukantainen peliloop käynnissä, jossa voi syottaa tekstiä
commands.py on luotu, jossa on komentojen tulevaa logiikkaa esitelty
test1 testaa, että commands.py toimii oikein

##viikko 4
Rooms.py on luotu, jossa luodaan lista "room" olioita peliä varten. Tiedot luetaan "rooms.csv" tiedostosta. Tiedostoa muuttamalla voisi siis tehdä eri tasoja pelattavaksi.
Lisäksi peli nyt tietää pelaajan sijainnin, ja muuttaa sitä oikein "move" komennolla, mikäli kerrotussa ilmansuunnassa on huone.
Look-komento antaa huoneen deskription.
(Tällä hetkellä on vain aloitushuone, ja toinen huone suunnassa south. Näiden välillä voi liikkua kirjoittamalla move south ja move north)

##viikko 5
Items.py on luotu. Toimii samalla logiikalla kuin Rooms.py. Komentoja esineiden etsimiseen, käyttämiseen, ja listaamiseen. (search, use {item}, items).
Huoneet voivat olla nyt lukossa, kuten huone Bathroom todistaa. (south, south, west, west)
Esineiden käyttäminen ei vielä tee mitään erityistä. Lisäksi search-komennon avulla voi saada rajattoman määrän esinettä, sillä se ei poistu huoneesta.
Testit toimivat 
