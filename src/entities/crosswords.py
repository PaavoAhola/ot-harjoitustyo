class Crossword:
    """Luokka, joka vastaa yksittäisen sanaristikon ominaisuuksista.
    
    Attributes:
        name: Ristikolle annettava nimi.
        creator: Ristikon luoneen käyttäjän nimi.
        highscores: Ristikon top-lista.
        squares: Lista Square-olioista, joista ristikko koostuu.
    """
    
    def __init__(self, name, creator):
        """ Luokan konstruktori, jonka tehtävä on luoda uusi ristikko.
        
        Args:
            name: Ristikolle annettava nimi.
            creator: Ristikon luoneen käyttäjän nimi.
        """
        
        self.name = name
        self.creator = creator
        self.highscores = []
        self.squares = []
        for i in range(10):
            self.squares.append([])
        for i in range(10):
            for j in range(10):
                self.squares[i].append(Square(i,j))

    def add_highscore(self, time, user):
        """Lisää tuloksen ristikon top-listalle, jos tulos riittävän hyvä.
        
        Args:
            time: Käyttäjän tulokseksi saama aika.
            user: Ristikon ratkaissut käyttäjä.
        """
        
        self.highscores.append((time, user))
        self.highscores.sort()
        if len(self.highscores) == 11:
            self.highscores.pop()

    def show_highscores(self):
        """Tulostaa ristikon parhaat tulokset, jos niitä on.
        
        """
        
        print(f"{self.name} by {self.creator}")
        tries = False
        for score in self.highscores:
            print(f"{score[1]}: {score[0]}")
            tries = True
        if not tries:
            print("Ei tuloksia")


class Square:
    """Luokka, joka kantaa yksittäisen ristikkoruudun tietoja.
    
    Attributes:
        letter: Ruudussa oleva kirjain.
        on: Kertoo, onko ruudussa kirjain vai vihje.
        position: Ruudun sijainti ristikossa.
        surface: Attribuutti, johon tallennetaan ruudun piirtämiseen tarvittavat tiedot.
        hint_right: Vinkki ruudusta oikealle menevään sanaan.
        hint_down: Vinkki ruudusta alaspäin menevään sanaan.
    """
    
    def __init__(self, x, y):
        """Luo uuden ristikkoruudun.
        
        Args:
            x: Ruudun x-koordinaatti.
            y: Ruudun y-koordinaatti.
        """
        
        self.letter = " "
        self.on = True
        self.position = (x,y)
        self.surface = None
        self.hint_right = ""
        self.hint_down = ""

    def switch(self):
        """Vaihtaa ruudun aktiivisesta epäaktiiviseksi tai päinvastoin.
        
        """
        
        if self.on:
            self.on = False
        else:
            self.on = True

    def insert_letter(self, x):
        """Asettaa ruutuun kirjaimen.
        
        Args:
            x: Ruutuun asetettava kirjain.
        """
        
        self.letter = x
