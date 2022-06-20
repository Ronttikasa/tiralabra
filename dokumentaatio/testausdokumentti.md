# Testausdokumentti

Sovellusta on testattu automaattisilla yksikkötesteillä. Sovellusta on testattu manuaalisesti myös end-to-end-tasolla [data-kansiosta](/data/input) löytyvällä testidatalla, jolla on pystytty toteamaan että sovellus toimii kokonaisuutena odotetulla tavalla. 

## Testien suorittaminen

Suorita testit komennolla:
```
poetry run invoke test
```

Generoi testikattavuusraportti komennolla:
```
poetry run invoke coverage-report
```

## Testikattavuus

Yksikkötestien testikattavuus seurattavissa Codecovissa: 
[![codecov](https://codecov.io/gh/Ronttikasa/tiralabra/branch/main/graph/badge.svg?token=JEOZCTXS7I)](https://codecov.io/gh/Ronttikasa/tiralabra)

## End-to-end-testaus ja Markovin ketjun asteiden vertailua

Ohjelman toimintaa on testattu data-kansiosta löytyvällä [testidatalla](/data/input/abc_test_data.txt) joka sisältää n. 15 eri reel-kappaletta [The Session](https://thesession.org/tunes) -sivustolta koottuna.

Seuraavat kaksi katkelmaa on generoitu kyseisestä opetusdatasta, toinen ensimmäisen ja toinen 9. asteen Markovin ketjulla:

![image](https://user-images.githubusercontent.com/44512829/174509912-e9ef49ca-2a11-4f3b-b078-7777188bb0b7.png)

```
X: 1
T: test reel 1
M: 4/4
L: 1/8
K: Dmaj
edec dedd|dedd aggf|dede dedA|Bdde gfde|dfed BADd|Bdfg ggge|gafa fede|dfgf degf|]
```

![image](https://user-images.githubusercontent.com/44512829/174509974-2ad59664-3e2a-4ac1-907a-983c4c1594ce.png)

```
X: 1
T: test reel 9
M: 4/4
L: 1/8
K: Dmaj
Gedc ABce|ddcd ddef|ffgf edcB|ggfg ggfe|dcBA Bcde|ddcd dded|ddAB AFAG|GFGE FDEf|]
```

Pikaisella tarkastelulla opetusdataa vasten oli todettavissa että ensimmäisen asteen ketjulla generoidussa sävelsarjassa on sellaisia sekvenssejä joita ei esiinny missään opetusdatassa, ja yhdeksännen asteen ketjulla on generoitunut katkelma Saint Anne's -reeliä, joka näyttää lopussa vaihtuvan The Mountain Road -kappaleeksi (minulle on vielä vähän hämärän peitossa miten tämä tapahtui koska noin pitkää yhteistä osiota kappaleilla ei mielestäni ole).
