# Viikkoraportti 4

Tällä viikolla olen toteuttanut sovellukselle tiedostonkäsittelyluokan sekä yksinkertaisen käyttöliittymän jonka avulla sovelluksen toimintaa voi testata käytännössä. Olen lisäksi kirjoittanut testejä saadakseni testikattavuuden järkevämmälle tasolle, ja testeillä löytyikin jo pari virhettä ohjelmasta.

Testien laatiminen on ollut opettavaista mutta myös haastavaa, erityisesti TrieService-luokan testaamisen kanssa minulla oli hankaluuksia, en osannut kirjoittaa mielestäni tarpeeksi "pieniä" testejä. Luokkaa testatessa tuli esim. eteen tilanne jossa testin opetusdatassa esiintyi aivan lopussa kolmikko jossa soinnut olivat uudenlaisessa järjestyksessä eikä trieen tullut tallennetuksi sitä miten kyseistä sekvenssiä voisi jatkaa. Tämä aiheutti ohjelman kaatumisen toisinaan ja onnistuin löytämään ongelman syyn vasta tutkimalla trieä ja muodostuvia sekvenssejä käsin, mutta en keksinyt vielä miten voisi varmistaa ettei ongelma toistu. Laajalla opetusdatalla lienee tosin epätodennäköistä että aivan viimeiseksi osuisi täysin uusi sekvenssi.

Seuraavaksi aion tehdä pieniä parannuksia musiikillisen rakenteen muodostamiseen - esim. sointusarjan voisi aloittaa ja lopettaa sävellajin mukaisesti vain sellaisista soinnuista joista opetusdatan kappaleet alkavat/loppuvat. Opetusdatan laajentamiseen pitäisi myös käyttää aikaa jotta ohjelmalla voi tehdä kiinnostavampia vertailuja eriasteisten Markovin ketjujen välillä.

Työaika n. 15 h
