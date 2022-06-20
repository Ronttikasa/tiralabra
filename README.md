# Tiralabra - sointugeneraattori

[![CI](https://github.com/Ronttikasa/tiralabra/actions/workflows/main.yml/badge.svg)](https://github.com/Ronttikasa/tiralabra/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/Ronttikasa/tiralabra/branch/main/graph/badge.svg?token=JEOZCTXS7I)](https://codecov.io/gh/Ronttikasa/tiralabra)

[Määrittelydokumentti](/dokumentaatio/maarittely.md)

[Viikkoraportti 1](/dokumentaatio/viikkoraportti1.md)

[Viikkoraportti 2](/dokumentaatio/viikkoraportti2.md)

[Viikkoraportti 3](/dokumentaatio/viikkoraportti3.md)

[Viikkoraportti 4](/dokumentaatio/viikkoraportti4.md)

[Viikkoraportti 5](/dokumentaatio/viikkoraportti5.md)

[Viikkoraportti 6](/dokumentaatio/viikkoraportti6.md)

## Reel-generaattori

Reel-generaattori on ohjelma joka muodostaa trie-tietorakennetta ja Markovin ketjuja hyödyntäen ohjelmalle syötettyyn opetusdataan perustuvaa musiikkia. Ohjelma hyödyntää [abc-notaatiota](https://abcnotation.com/blog/2010/01/31/how-to-understand-abc-the-basics/), jota käytetään mm. kansanmusiikin notaatioon nuottiviivastonotaation sijasta/ohella.


### Ohjelman asennus:

- Kloonaa repositorio, ja asenna riippuvuudet komennolla `poetry install`.
- Suorita ohjelma komennolla `poetry run invoke start`.
- Repositorion _data_-hakemistossa on tiedosto nimeltä _abc_test_data.txt_ jota voi käyttää opetusdatana ohjelmaa kokeillessa. 
- Ohjelma tallentaa generoidun musiikin käyttäjän antaman nimen nimiseen tiedostoon _data/output_-hakemistoon.


