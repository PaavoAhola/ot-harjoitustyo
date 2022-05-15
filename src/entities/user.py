class User:
    """Sovelluksen käyttäjää kuvaava luokka.
    
    Attributes:
        __name: Käyttäjän nimi.
        __password: Käyttäjän salasana.
    """
    
    def __init__(self, name, password):
        """Konstruktori, joka luo käyttäjäolion.
        
        Args:
            name: Käyttäjän nimi.
            password: Käyttäjän salasana.
        """
        
        self.__name = name
        self.__password = password

    def return_name(self):
        """Palauttaa käyttäjän nimen.
        
        Returns:
            Käyttäjän nimi.
        """
        
        return self.__name
