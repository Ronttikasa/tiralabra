# Testausdokumentti

Sovellusta on testattu automaattisilla yksikkötesteillä. Sovellusta on testattu manuaalisesti myös end-to-end-tasolla [data-kansiosta](/data/input) löytyvällä testidatalla, jolla on pystytty toteamaan että sovellus toimii kokonaisuutena odotetulla tavalla. Yksikkötesteillä on esimerkiksi varmistettu että ohjelman generointialgoritmin luomat sekvenssit löytyvät opetusdatasta.

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

![image](https://user-images.githubusercontent.com/44512829/176534360-f76bf92b-0cd5-4cae-8bbf-77b92e18b0ea.png)

Yksikkötestien testikattavuus tarkemmin Codecovissa: 
[![codecov](https://codecov.io/gh/Ronttikasa/tiralabra/branch/main/graph/badge.svg?token=JEOZCTXS7I)](https://codecov.io/gh/Ronttikasa/tiralabra)

## End-to-end-testaus ja Markovin ketjun asteiden vertailua

Ohjelman toimintaa on testattu data-kansiosta löytyvällä [testidatalla](/data/input/abc_test_data.txt) joka sisältää n. 15 eri reel-kappaletta [The Session](https://thesession.org/tunes) -sivustolta koottuna.

Seuraavat katkelmat on generoitu kyseisestä opetusdatasta, eri Markovin ketjun asteilla:

1. asteen Markovin ketju:

![image](https://user-images.githubusercontent.com/44512829/174509912-e9ef49ca-2a11-4f3b-b078-7777188bb0b7.png)

```
X: 1
T: test reel 1
M: 4/4
L: 1/8
K: Dmaj
edec dedd|dedd aggf|dede dedA|Bdde gfde|dfed BADd|Bdfg ggge|gafa fede|dfgf degf|]
```

5. asteen Markovin ketju:

![image](https://user-images.githubusercontent.com/44512829/174636646-fff3caf6-9b9b-481a-995b-cc54804e0c25.png)

```
X: 1
T: test tune
M: 4/4
L: 1/8
K: Dmaj
BAFA FABc|dddA BAFA|Addd Addd|AddA BAFA|ABde fBBA|Bcde defa|afde dBdA|AFGA BcdB|]
```

9. asteen Markovin ketju:

![image](https://user-images.githubusercontent.com/44512829/174509974-2ad59664-3e2a-4ac1-907a-983c4c1594ce.png)

```
X: 1
T: test reel 9
M: 4/4
L: 1/8
K: Dmaj
Gedc ABce|ddcd ddef|ffgf edcB|ggfg ggfe|dcBA Bcde|ddcd dded|ddAB AFAG|GFGE FDEf|]
```

Pikaisella tarkastelulla opetusdataa vasten oli todettavissa että ensimmäisen asteen ketjulla generoidussa sävelsarjassa on esimerkiksi sellaisia neljän sävelen sekvenssejä joita ei esiinny sellaisenaan opetusdatassa. Ensimmäisellä asteella myös kuulokuva vaikuttaa selvästi satunnaisemmin etenevältä kuin muissa esimerkeissä. Viidennen asteen näytteestä tunnistin pieniä pätkiä kappaleista _The Concertina_, _The Maid Behind the Bar_, _The Bucks of Oranmore_ ja _Sally Gardens_. Neljännellä asteella näytteessä esiintyi jo kuutta eri kappaletta.

Tässä tapauksessa yhdeksännen asteen ketjulla on generoitunut katkelma _Saint Anne's_ -reeliä, joka näyttää lopussa vaihtuvan _The Mountain Road_ -kappaleeksi. Reelit ovat tyypillisesti melko samantyyppisiä kappaleita, joten korkeahkoillakin asteilla on mahdollista saada materiaalia useammasta opetusdatan kappaleesta, mutta tämä toki riippuu opetusdatasta sekä sattumasta. Esimerkiksi kahdeksannella asteella tehty testi puolestaan sisälsi materiaalia vain yhdestä kappaleesta.

Yhdeksännen asteen näytekään ei suoraan kuulosta _Saint Anne's_ -reeliltä sillä sävelet osuvat eri tahdinosille, mutta nuottikuvia katsomalla yhdenmukaisuus on helppo nähdä. Mielekkäintä reelien generointi tällä tekniikalla kuitenkin lienee kolmannen ja neljännen asteen tienoilla, jolloin musiikki ei kuulosta täysin sattumanvaraiselta, mutta seuraavan sävelen valinnassa käytettävät sekvenssit ovat n. puolen tahdin mittaisia, joten opetusdatan yksittäiset kappaleet eivät vain kopioidu mukaan sellaisenaan.
