# Tiralabra - sointugeneraattori

[![CI](https://github.com/Ronttikasa/tiralabra/actions/workflows/main.yml/badge.svg)](https://github.com/Ronttikasa/tiralabra/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/Ronttikasa/tiralabra/branch/main/graph/badge.svg?token=JEOZCTXS7I)](https://codecov.io/gh/Ronttikasa/tiralabra)

[Määrittelydokumentti](/dokumentaatio/maarittely.md)

[Viikkoraportti 1](/dokumentaatio/viikkoraportti1.md)

[Viikkoraportti 2](/dokumentaatio/viikkoraportti2.md)

[Viikkoraportti 3](/dokumentaatio/viikkoraportti3.md)

[Viikkoraportti 4](/dokumentaatio/viikkoraportti4.md)

## Sointugeneraattori

Sointugeneraattori on ohjelma joka muodostaa trie-tietorakennetta ja Markovin ketjuja hyödyntäen ohjelmalle syötettyyn opetusdataan perustuvaa musiikkia. Toistaiseksi ohjelma operoi tekstitiedostoilla ja reaalisointumerkeillä, ja musiikillisen mielekkyyden tarkastelu pitää tehdä perinteisin menetelmin, mutta ohjelmaa on mahdollista muokata käyttämään esimerkiksi miditiedostoja.

Ohjelman asennus:

- Kloonaa repositorio, ja asenna riippuvuudet komennolla `poetry install`.
- Suorita ohjelma komennolla `poetry run invoke start`.
- Repositorion _data_-hakemistossa on tiedosto nimeltä _test_data.txt_ jota voi käyttää opetusdatana ohjelmaa kokeillessa. (Huom. esimerkkidata on varsin suppea). 
- Ohjelma tallentaa generoidun sointusarjan käyttäjän antaman nimen nimiseen tiedostoon _data/output_-hakemistoon.

Esimerkki ohjelmalle annettavista syötteistä:
![image](https://user-images.githubusercontent.com/44512829/172072912-428131a3-6ea1-4baf-94a2-c6305ac603e6.png)
