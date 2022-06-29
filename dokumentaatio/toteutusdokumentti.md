# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelma on toteutettu kerrosarkkitehtuurin mukaisesti. Käyttöliittymästä vastaa [UI-luokka](/src/ui.py), sovelluslogiikasta luokat [AppLogic](/src/app_logic.py) ja [TrieService](/src/trie_service.py) sekä trie-tietorakenteen toteutuksesta vastaavat luokat [TrieNode ja Trie](/src/trie.py). Tiedostojen käsittelyn hoitaa luokka [FileService](/src/file_service.py). 

## Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)

tbd

## Työn mahdolliset puutteet ja parannusehdotukset

ABC-notaation parserista puuttuu muutama sellainen ominaisuus joiden avulla sitä voisi huoletta käyttää minkä tahansa abc-nuotin lukemiseen - se ei esimerkiksi osaa lainkaan käsitellä sävellajiin kuulumattomia ylennys- ja alennusmerkintöjä eikä kertauksien maaleja. Tämän vuoksi testidataakin piti jonkin verran valikoida, toisaalta onneksi kansanmusiikki usein käyttää aika kiltisti pelkkiä sävellajin säveliä, toisaalta nyt myöskään generoituun musiikkiin ei tule mausteeksi mukaan muunnesäveliä.

Ohjelmaa voisi laajentaa antamalla käyttäjälle mahdollisuus valita mitä logiikkaa ohjelma käyttää muodostaessaan sävelsekvenssejä. Nykymuodossaan trie-rakenteessa pidetään kirjaa kutakin säveltä seuraavien sävelten frekvenssistä ja seuraavan sävelen arvonta tapahtuu näiden frekvenssien painottamana. Seuraava sävel olisi kuitenkin mahdollista arpoa esimerkiksi tasatodennäköisyyksillä tai painottamalla pienintä frekvenssiä.

Ohjelma ei validoi käyttäjän antamia syötteitä.

## Lähteet

- [Trie, Wikipedia](https://en.wikipedia.org/wiki/Trie)
- [ABC-notaatio](https://abcnotation.com/blog/2010/01/31/how-to-understand-abc-the-basics/)
