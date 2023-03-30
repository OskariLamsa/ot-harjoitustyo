```mermaid
classDiagram
class Pelaajat{
 +string nappula
 +string ruutu
 }
class Pelilauta{
 +list ruudut
 }
 class Ruutu{
 +ruutu seuraavaruutu
 }
 class Pelinappula{
  +string nimi
  +string sijainti
