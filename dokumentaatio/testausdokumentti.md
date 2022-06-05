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
