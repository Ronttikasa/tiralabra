# Käyttöohje

## Ohjelman asennus:

- Kloonaa repositorio tai lataa uusin release, ja asenna riippuvuudet komennolla `poetry install`.
- Käynnistä ohjelma komennolla `poetry run invoke start`.

## Ohjelman käyttö:

- Ohjelman päänäkymässä on kaksi toimintoa: uuden opetudatatiedoston syöttäminen (r) sekä ohjelman lopettaminen (q).
- Ohjelma pyytää käyttäjältä syötteinä opetusdatatiedoston nimen, korkeimman käytettävän Markovin ketjun asteen, sekä generoitavan kappaleen nimen ja pituuden.
- Esimerkki ohjelman käytöstä: ![image](https://user-images.githubusercontent.com/44512829/176536163-bfbd1e46-53aa-4d8c-8e77-67986c0b92b6.png)

- Repositorion _data_-hakemistossa on tiedosto nimeltä [_abc_data.txt_](/data/input/abc_data.txt) jota voi käyttää opetusdatana ohjelmaa kokeillessa. 
- Ohjelma tallentaa generoidun musiikin käyttäjän antaman nimen mukaisiin tiedostoihin _data/output_-hakemistoon, numeroituna Markovin ketjun asteen mukaan.

## Opetusdata

Ohjelma käyttää [ABC-muotoista](https://abcnotation.com/blog/2010/01/31/how-to-understand-abc-the-basics/) opetusdataa, jota on helppo löytää esimerkiksi [The Session](https://thesession.org/tunes) -sivustolta, jonka haulla kappaleita voi  suodattaa esimerkiksi sävellajin ja rytmityypin mukaan. Jos opetusdatassa käytetään useampaa kappaletta, on mielekästä valita kaikki kappaleet samasta sävellajista. Kappaleet tallennetaan samaan tekstitiedostoon jossa jokainen ABC-formaatin rivi alkaa omalta riviltään. Mallia voi katsoa esimerkkitiedostosta.

### Rajoituksia opetusdatalle

Ohjelmaan kirjoittamani ABC-parseri ei osaa tulkita kaikkia ABC-notaation merkintöjä, olennaisimmat puutteet ovat tuki alennus- ja ylennysmerkeille (^ _ =)   sekä kertausmaaleille (esim. |1 ja `[2`). Jos opetusdatassa on näitä merkintöjä, ohjelma ei välttämättä toimi täysin oikein. ABC-notaatiossa sävellajia käsitellään kuitenkin implisiittisesti (esimerkiksi G-duurissa merkintä `f` tarkoittaa sävellajiin kuuluvaa fis-säveltä) joten ylennys- ja alennusmerkkien puuttuminen ei ole niin valtaisa puute kuin miltä se kuulostaa. Lähinnä se rajoittaa sävellajiin kuulumattomien sävelten käyttöä.
