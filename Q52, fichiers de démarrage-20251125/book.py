class Book:
    """
    ébauche de classe Book, à développer suivant les consignes
    """
    def __init__(self, title, author, publication_year, page_count, country,language, rental_price, isbn, is_available, wikipedia_url):
        self.__title = title
        self.__author= author
        self.__publication_year = publication_year
        self.__page_count = page_count
        self.__country = country
        self.__language= language
        self.__rental_price= rental_price
        self.__isbn= isbn
        self.__is_available = is_available
        self.__wikipedia_url = wikipedia_url

    def __str__(self):
        return (f"Titre: {self.title}, Auteur: {self.author}, "
                f"Année: {self.__publication_year}, Pages: {self.__page_count}, "
                f"Emprunté: {'Oui' if not self.is_available else 'Non'}")
    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def publication_year(self):
        return self.__publication_year
    
    @property
    def page_count(self):
        return self.__page_count
    
    @page_count.setter
    def page_count(self, value):
        if value > 0:
            self.__page_count = value
    
    @property
    def country(self):
        return self.__country
    
    @property
    def language(self):
        return self.__language
    
    @property
    def rental_price(self):
        return self.__rental_price
    
    @property
    def isbn(self):
        return self.__isbn
    
    @property
    def is_available(self):
        return self.__is_available
    
    @property
    def wikipedia_url(self):
        return self.__wikipedia_url
    
    def emprunter(self):
        if self.__is_available:
            self.__is_available = False
            return f"Le livre '{self.__title}' a été emprunté."
        else:
            return f"Le livre '{self.__title}' est déjà emprunté."

    def retourner(self):
        if not self.is_available:
            self.__is_available = True
            return f"Le livre '{self.__title}' a été retourné."
        else:
            return f"Le livre '{self.__title}' n'était pas emprunté."

@author.setter
def author(self, value):
    self.__author = value

if __name__ == '__main__':
    #
    livre1 = Book("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, 96,   "France", "FR", 1, "978-2-07-061275-8", True,
    "https://fr.wikipedia.org/wiki/Le_Petit_Prince")
    print(livre1)
    print(f"\nEmprunt :  {livre1.emprunter()}")
    print(livre1)
    print(f"\nRetour: {livre1.retourner()}")
    print(livre1)
    #
    pass


