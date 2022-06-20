# Viikkoraportti 6

Tällä viikolla pääsin taas paremmin kiinni projektiin sekä aikataulun että projektin sisällön suhteen ohjaajan kanssa käydyn keskustelun jälkeen. Tutkiskelin jonkin aikaa Lilypondia, mutta epäilin etten onnistu löytämään sopivaa opetusdataa. Harrastelen silloin tällöin irlantilaisen kansanmusiikin soittamista ja muistin [The Session](https://thesession.org/tunes) -sivuston ja siellä käytetyn erikoisen [notaatiotavan](https://abcnotation.com/blog/2010/01/31/how-to-understand-abc-the-basics/).

Ohjelma on nyt melko käyttökelpoisella mallilla, se ottaa sisään abc-muodossa olevaa dataa (ks. [esimerkkitiedosto](/data/input/abc_test_data.txt)) ja muodostaa samanlaisen tiedoston joka on mahdollista sekä kääntää nuoteiksi että soittaa jollakin abc-notaatiota ymmärtävällä ohjelmalla - esim. [Colin Humen nettisivusto](https://colinhume.com/Music.aspx). Yksikkötestaus on myös edistynyt, joskin olen nyt raskaasti priorisoinut sitä että saan ohjelman demottavaan kuntoon, joten testaus on jonkin verran jäljessä. Rivikattavuus testeillä on kuitenkin n. 70% eli ei aivan katastrofaalinen.

Korkeilla Markovin ketjun asteilla generointi näyttää mahdollisesti tekevän jotakin erikoista, yritän seuraavaksi selvitellä asiaa tarkemmin, sekä päivitän testausta ja dokumentaatiota.

Ajankäyttöarvio 15 h
