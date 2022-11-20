# TurQuiz - Tietovisa-sovellus

Sovelluksen idea on ratkaista eri aihepiirien tietovisoja. Visat ovat joko käyttäjän itse, tai muiden käyttäjien luomia.
Käyttäjä näkee kokonaispisteensä vastattuaan tietovisaan, mutta ei oikeita tai vääriä vastauksia eroteltuina.

Sovelluksen ominaisuuksia ovat:

* Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
* Käyttäjä näkee kaksi erillistä listaa: Omat visat ja Community visat.
* Käyttäjä voi filtteröidä visoja hakusanalla.
* Käyttäjä voi pelata näkyvilla olevia visoja.
    * Pelaaminen tapahtuu täyttämällä lomake, joka palautetaan lopuksi. Lomakkeen palautettuaan käyttäjä näkee omat pisteensä, sekä oman highscorensa.
* Käyttäjä voi luoda omia visoja, jotka voivat olla joko private tai public.
    * Visaa luodessa käyttäjä antaa kysymyksen ja neljä vastausvaihtoehtoa, joista yksi on oikea.

## Välipalautus 2. (20.11)

### Sovelluksen nykytila:
* Käyttäjä voi kirjautua sisään ja ulos, sekä luoda uuden tunnuksen.
* Käyttäjä näkee kaksi erillistä listaa: omat visat ja julkiset visat.
* Käyttäjän on mahdollista luoda omia visoja, jotka hän voi asettaa joko julkiseksi tai yksityiseksi.
    * Visaa luodessa käyttäjä antaa aihepiirin ja valitsemansa määrän kysymyksiä joissa on neljä vastausvaihtoehtoa.

### Seuraavat kehitysaskeleet:
* Visoihin ei pysty vielä vastaamaan, niitä voi ainoastaan luoda.
* Luotuja visoja ei pysty muokkaamaan, eikä poistamaan.
* Visoja ei pysty filtteröidä hakusanalla.

* Koodi on vielä tässä vaiheessa sotkuista, ja esim. app.py tiedostoa ei ole hajautettu erillisiin moduuleihin.
* SQL komennot on tällä hetkellä db.Model queryillä, eikä puhtailla SQL komennoilla.
* Template tiedostoissa on suuri määrä copypastea <style> tägien sisällä.
* Kurssin fly.io ongelmista johtuen sovellus ei ole vielä testattavissa tuotannossa.

