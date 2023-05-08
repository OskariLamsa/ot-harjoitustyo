# Tekstiseikkailu
Klassinen tekstiseikkailu peli, jossa pelaaja voi pelata kirjoittamalla komentoja syotekenttään. Pygame mahdolllistaa grafiikan piirtämiseen, joten sen avulla esitetään erinlaisia elementtejä kuten pelaajan elämäpisteet ja rahat.

## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmäärittely.md)
- [Kirjanpito](./dokumentaatio/tuntikirjaus)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Peliohje](./dokumentaatio/peliohje.md)

## Asennus
Voit asentaa riippuvuudet ja ajaa pelin seuraavilla komennoilla:
```bash
poetry install
```
```bash
poetry run invoke start
```
Jos haluat resetoida pelin tallenustiedoston, kirjoita:
```bash
poetry run invoke reset
```
Jos haluat resetoida ja pelata, voit kirjoittaa:
```bash
poetry run invoke resetstart
```

## Testit
HUOM: resetoi ennen kuin suoritat testejä!
Voit ajaa pylint testit komennolla:
```bash
poetry run invoke pylint
```
Coverage-raportin saa komennolla:
```bash
poetry run coverage-report
```
