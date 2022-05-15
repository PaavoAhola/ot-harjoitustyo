# Käyttöohje

Lataa sovelluksen lähdekoodi viimeisimmän releasen avulla.

## Sovelluksen käynnistäminen

Riippuvuudet asennetaan komennolla
```bash
poetry install
```

Alusta sovelluksen toiminta komennolla
```bash
poetry run invoke build
```

Käynnistä sovellus komennolla
```bash
poetry run invoke start
```

## Tekstikäyttöliittymä

Sovellusta käytetään terminaalista käsin. Käynnistämisen jälkeen terminaaliin tulostuu ohjeita, joihin käyttäjä kirjoittaa vastaukset, joiden mukaan sovellus toteuttaa itseään. Vastausvaihtoehdot tulostetaan terminaaliin. Käyttäjän riittää kirjoittaa sopivan vaihtoehdon numero tai nimi tekstikenttään ja painaa ENTER. Sovellus sulkeutuu kun käyttäjä kirjautuu ulos. Kirjautumisen ja uuden käyttäjän luomisen ohjeet tulostetaan, kun sovellus käynnistyy.

## Ristikot (graafinen käyttöliittymä)

Kun käyttäjä päättää luoda tai ratkaista sanaristikon, näkymä vaihtuu graafiseen Pygame-käyttöliittymään. Myös ristikkonäkymässä käyttäjälle tulostetaan ohjeita, miten edetä sovelluksen kanssa. Ristikossa valitaan nuolinäppäimillä ruutu, johon tehdään muutoksia. Ristikkonäkymästä poistutaan painamalla hiirellä ruudun oikean yläkulman x-painiketta.

### Ristikon laatiminen
Ristikkoa laadittaessa ruutuja voidaan aktivoida käyttöön tai sulkea vihjeruuduiksi. Vihjeruutuihin voi kirjoittaa vihjeitä painamalla + -painiketta. Vihjettä kirjoittaessa käyttäjän on siirryttävä terminaaliin kirjoittamaan vihje. Kun vihje on kirjoitettu ja syötetty painamalle ENTER, käyttäjän tulee siirtyä takaisin ristikko-ikkunaan. Siirtymän ikkunoiden välillä voi suorittaa hiiren avulla. Kun käyttäjä lopettaa ristikon laatimisen (painamalla hiirellä x), ohjelma kysyy, haluaako käyttäjä julkaista ristikon muiden käyttäjien näkyviin, tallentaa ristikon omaa jatkokehittämistä varten vai hylätä luonnoksen.
**HUOM!** Kun julkaiset ristikon muille käyttäjille, täytä ristikko oikeilla kirjaimilla. Näin sovellus tietää ristikon oikean ratkaisun ja voi pitää yllä tuloksia muilta käyttäjiltä.

### Ristikon ratkominen
Ristikkoa ratkottaessa ruutuja ei voi aktivoida eikä niihin voi kirjoittaa vihjeitä. Ruutuihin voi ainoastaan lisätä kirjaimia. Kun käyttäjä lopettaa ristikon täyttämisen, sovellus tarkistaa, onko ristikko ratkaistu oikein. Jos on, sovellus ilmoittaa käytetyn ajan ja lisää käyttäjän tuloksen kyseisen ristikon tilastoihin, jos aika pääsee kymmenen parhaan ajan joukkoon.

## Sovelluksen sulkeminen
Sovellus sulkeutuu, kun käyttäjä kirjautuu ulos alkunäkymässä.
