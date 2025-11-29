import json
from book import Book

class Library:
    """
    la classe Library à développer suivant les consignes
    """

    def __init__(self, file_in ):
        self.__library_l = []
        self.__load_books_from_json(file_in)
            # ....

    
    def __str__(self):
        total_books = len(self.__library_l)
        availble_books = 0
        for book in self.__library_l:
            if book.is_available:
                availble_books += 1
        borrowed_books = total_books - availble_books
        result = f"=== BIBLIOTHÈQUE ===\n"
        result += f"Total de livres: {total_books}\n"
        result += f"Disponibles: {availble_books}\n"
        result += f"Empruntés: {borrowed_books}\n"

        return result
    # ....
    @property
    def library_l(self):
        """Retroune la liste des livres (en lecture seule)"""
        return self.__library_l
    
    def __load_books_from_json(self, file_in):
        """
        Charge les livres depuis un fichier JSON et crée des objets Book
        :param file_in: chemin vers le fichier JSON
        """
        try:
            with open(file_in, 'r', encoding='utf-8') as file:
                books_data = json.load(file)
                
                for book_data in books_data:
                    book = Book(**book_data)
                    self.__library_l.append(book)
                    
            print(f"✅ {len(self.__library_l)} livres chargés avec succès!")
            
        except FileNotFoundError:
            print(f"Erreur: Le fichier '{file_in}' n'a pas été trouvé.")
        except json.JSONDecodeError:
            print(f"Erreur: Le fichier '{file_in}' n'est pas un JSON valide.")
        except KeyError as e:
            print(f"Erreur: Clé manquante dans le JSON: {e}")

    # Consigne 2 : Affichage de tous les livres
    def display_books_all(self):
        """
        Affiche tous les livres de la bibliothèque , on tri
        """
        sorted_books = sorted(self.__library_l, key=lambda book: book.page_count,  reverse=True)
        #Affichage de l en-tête
        print(f"{'Titre':<50} {'Auteur':<30} {'Pages':<10} {'Année':<10} {'Disponible':<12}")
        print("-" * 112)
        #Parcourir les livres triés
        for book in sorted_books:
            availability = 'Oui' if book.is_available else 'Non'
            print(f"{book.title:<50} {book.author:<30} {book.page_count:<10} {book.publication_year:<10} {availability:<12}")

    #Consigne 3 : Affichage des livres commençant par une lettre donnée
    def display_books_over_400_pages(self):
        """
        Affiche les livres ayant plus de 400 pages
        """
        filtered_books = []
        #Parcourir tous les livres et garder ceux plus de 400 pages
        for book in self.__library_l:
            if book.page_count > 400:
                filtered_books.append(book)
        #Tri par ordre croissant
        sorted_books = sorted(filtered_books, key= lambda book: book.page_count)
        print(f"{'Titre':<50} {'Auteur':<30} {'Pages':<10} {'Année':<10} {'Disponible':<12}")
    print("-" * 112)
        #Maintenant on va afficher chauqe livre
    for book in sorted_books:
            availability = 'Oui' if book.is_available else 'Non'
            print(f"{book.title:<50} {book.author:<30} {book.page_count:<10} {book.publication_year:<10} {availability:<12}")

    #Consigne 4
    def display_french_authors_books(self):
        """
        Affiche les livres écrits par des auteurs français
        """
    french_authors = ["Victor Hugo", "Alexandre Dumas", "Guy de Maupassant",  "Antoine de Saint-Exupéry", 
    "Gustave Flaubert", "Jules Verne", "Émile Zola", "Stendhal", "Albert Camus", "Charles Baudelaire", "Bernard Werber"]
    
    # Filtrer les livres
    filtered_books = []
    for book in self.__library_l:
        # Comment vérifier si l'auteur du livre est dans la liste french_authors ?
        for book in self.__library_l:
    # Comment vérifier si l'auteur du livre est dans la liste french_authors ?
            if book.author in french_authors:
                filtered_books.append(book)
    
    print(f"{'Titre':<50} {'Auteur':<30} {'Pages':<10} {'Année':<10} {'Disponible':<12}")
print("-" * 112)

for book in sorted_books:
    availability = 'Oui' if book.is_available else 'Non'
    print(f"{book.title:<50} {book.author:<30} {book.page_count:<10} {book.publication_year:<10} {availability:<12}")
    
    # Trier par titre (ordre alphabétique)
    sorted_books = sorted(filtered_books, key=lambda book: book.title)
    # Afficher les 3 premiers livres
    print("\nLes 3 premiers livres:")
    for i, book in enumerate(test_library.library_l[:3]):
        print(f"{i+1}. {book}")
    #
    pass
def update_old_books_author(self):
    """
    Met à jour l'auteur des livres publiés avant 1850 à "Auteur Inconnu"
    """
    count = 0
    for book in self.__library_l:
        if book.publication_year < 1850:
            book.author = "Auteur Inconnu"
            count += 1
    
    print(f"{count} livre(s) mis à jour avec 'Auteur Inconnu'")

def return_three_words_books(self):
    """
    Retourne tous les livres dont le titre contient exactement 3 mots
    """
    count = 0
    
    for book in self.__library_l:
        # Comment compter le nombre de mots dans le titre ?
        words = book.title.split()  # Divise le titre en mots
        
        if len(words) == 3:
            # Le livre a exactement 3 mots dans le titre
            # Mais on ne peut retourner que les livres empruntés !
            if not book.is_available:  # Si le livre est emprunté
                result = book.retourner()
                print(result)
                count += 1
    
    print(f"\n✅ Total: {count} livre(s) retourné(s)")

def __len__(self):
    """
    Méthode magique qui retourne le nombre total de pages des livres
    publiés avant 1900 et qui sont empruntés
    """
    total_pages = 0
    
    for book in self.__library_l:
        if book.publication_year < 1900 and not book.is_available:
            total_pages += book.page_count
    
    return total_pages

def save_to_json(self, filename="book_out.json"):
    """
    Sauvegarde la bibliothèque dans un fichier JSON
    """
    books_data = []
    
    for book in self.__library_l:
        book_dict = {
            "title": book.title,
            "author": book.author,
            "publication_year": book.publication_year,
            "page_count": book.page_count,
            "country": book.country,
            "language": book.language,
            "rental_price": book.rental_price,
            "isbn": book.isbn,
            "is_available": book.is_available,
            "wikipedia_url": book.wikipedia_url  # Pas de virgule après le dernier élément
        }  # <-- N'oubliez pas de fermer l'accolade
        books_data.append(book_dict)
    
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(books_data, file, ensure_ascii=False, indent=4)
    
    print(f"✅ Bibliothèque sauvegardée dans '{filename}'")