```mermaid
classDiagram
class Pelaajat{
 +string nappula
 +string ruutu
 +int rahat
 }
class Pelilauta{
 +list ruudut
 }
 class Ruutu{
 +ruutu seuraavaruutu
 +tyyppi ruututyyppi
 }
 class Pelinappula{
  +string nimi
  +string sijainti
 }
 class Aloitusruutu{
 +string nimi
 +anna_200e()
 }
 class Vankila{
 +string nimi
 +saako_pelaaja_liikkua()
 }
 class Sattuma ja yhteismaa{
 +string nimi
 +hae_sattumakortti()
 +hae_yhteismaakortti()
 }
 class Asemat ja laitokset{
 +string nimi
 +tee_jotain()
 }
 class Normaalit kadut{
 +string nimi
 +list talot
 +bool hotelli
 }
Pelaajat --> Pelinappula
Pelaajat --> Ruutu
Pelilauta --> Ruutu
Ruutu --> Ruutu
Ruutu --> Aloitusruutu
Ruutu --> Vankila
Ruutu --> Sattuma ja yhteismaa
Ruutu --> Asemat ja laitokset
Ruutu --> Normaalit kadut
