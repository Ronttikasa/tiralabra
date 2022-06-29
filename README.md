# Tiralabra - musiikkigeneraattori

[![CI](https://github.com/Ronttikasa/tiralabra/actions/workflows/main.yml/badge.svg)](https://github.com/Ronttikasa/tiralabra/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/Ronttikasa/tiralabra/branch/main/graph/badge.svg?token=JEOZCTXS7I)](https://codecov.io/gh/Ronttikasa/tiralabra)

## Reel-generaattori

Reel-generaattori on ohjelma joka muodostaa trie-tietorakennetta ja Markovin ketjuja hyödyntäen ohjelmalle syötettyyn opetusdataan perustuvaa musiikkia. Ohjelma hyödyntää [abc-notaatiota](https://abcnotation.com/blog/2010/01/31/how-to-understand-abc-the-basics/), jota käytetään mm. kansanmusiikin notaatioon nuottiviivastonotaation sijasta/ohella.


### Ohjelman asennus:

- Kloonaa repositorio, ja asenna riippuvuudet komennolla `poetry install`.
- Suorita ohjelma komennolla `poetry run invoke start`.
- Repositorion _data_-hakemistossa on tiedosto nimeltä _abc_test_data.txt_ jota voi käyttää opetusdatana ohjelmaa kokeillessa. 
- Ohjelma tallentaa generoidun musiikin käyttäjän antaman nimen nimiseen tiedostoon _data/output_-hakemistoon.

Tutustu myös tarkempaan [käyttöohjeeseen](/dokumentaatio/kayttoohje.md).

[Määrittelydokumentti](/dokumentaatio/maarittely.md)

[Testausdokumentti](/dokumentaatio/testausdokumentti.md)

[Toteutusdokumentti](/dokumentaatio/toteutusdokumentti.md)
