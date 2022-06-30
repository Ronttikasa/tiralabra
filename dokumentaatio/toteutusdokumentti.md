# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelman perustoiminnallisuus käyttää itse toteutettua trie-tietorakennetta sekä algoritmia jonka avulla on mahdollista muodostaa Markovin ketjuja.

Ohjelma on toteutettu kerrosarkkitehtuurin mukaisesti. Käyttöliittymästä vastaa [UI-luokka](/src/ui.py), sovelluslogiikasta luokat [AppLogic](/src/app_logic.py) ja [TrieService](/src/trie_service.py) sekä trie-tietorakenteen toteutuksesta vastaavat luokat [TrieNode ja Trie](/src/trie.py). Tiedostojen käsittelyn hoitaa luokka [FileService](/src/file_service.py).

## Saavutetut aikavaativuudet

Trieen lisääminen:
```
procedure insert_sequence(sequence):
    current_node = root
    for note in sequence:
        if note in current_node.children:
            current_node.children[note].add_occurrence
        else:
            current_node.add_child(note)
        current_node = current_node.children[note]
```

Seuraavien mahdollisten arvojen hakeminen triestä:
```
function find_next_values(sequence):
    current_node = root
    for note in sequence:
        if note in current_node.children:
            current_node = current_node.children[note]
        else:
            return null
    return current_node.children
```

Sekä lisääminen että hakeminen toimivat käytännössä O(_n_)-ajassa eli riippuvat lisättävän/haettavan sekvenssin pituudesta, sillä trie-noden lapsisolmut on tallennettu Pythonin sanakirjarakenteena, jonka läpikäynnin aikavaativuus on keskimäärin O(1). Solmujen mahdollisten arvojen määrä on rajallinen, joten lapsisolmut olisi mahdollista tallettaa myös vakiomittaisena listana, joka vielä tehostaisi lisäämistä ja hakemista.


## Työn mahdolliset puutteet ja parannusehdotukset

ABC-notaation parserista puuttuu muutama sellainen ominaisuus joiden avulla sitä voisi huoletta käyttää minkä tahansa abc-nuotin lukemiseen - se ei esimerkiksi osaa lainkaan käsitellä sävellajiin kuulumattomia ylennys- ja alennusmerkintöjä eikä kertauksien maaleja. Tämän vuoksi testidataakin piti jonkin verran valikoida, toisaalta onneksi kansanmusiikki usein käyttää aika kiltisti pelkkiä sävellajin säveliä, toisaalta nyt myöskään generoituun musiikkiin ei tule mausteeksi mukaan muunnesäveliä.

Ohjelmaa voisi laajentaa antamalla käyttäjälle mahdollisuus valita mitä logiikkaa ohjelma käyttää muodostaessaan sävelsekvenssejä. Nykymuodossaan trie-rakenteessa pidetään kirjaa kutakin säveltä seuraavien sävelten frekvenssistä ja seuraavan sävelen arvonta tapahtuu näiden frekvenssien painottamana. Seuraava sävel olisi kuitenkin mahdollista arpoa myös esimerkiksi tasatodennäköisyyksillä tai painottamalla pienintä frekvenssiä.

Jatkokehityksessä ohjelmaa voisi myös laajentaa tukemaan paremmin muita tahtilajeja. Reel on 4/4-tahtilajinen tanssikappale, mutta irlantilaisessa kansanmusiikissa yleisiä ovat myös esimerkiksi 6/8-tahtilajiset jigit ja 9/8-tahtilajiset slip jigit.

Ohjelma ei validoi käyttäjän antamia syötteitä.

## Lähteet

- [Trie, Wikipedia](https://en.wikipedia.org/wiki/Trie)
- [ABC-notaatio](https://abcnotation.com/blog/2010/01/31/how-to-understand-abc-the-basics/)
- [Markov chain](https://en.wikipedia.org/wiki/Markov_chain)
