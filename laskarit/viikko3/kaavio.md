```mermaid
title: Monopoly1
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
 }
Pelaajat --> Pelinappula
