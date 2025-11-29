import library

# Création de l'instance
maBiblio = library.Library("book_in.json")
print(maBiblio)  # état initial

# Consigne 2 : Affichage initial
print("\n=== AFFICHAGE INITIAL ===")
maBiblio.display_books_all()

# Consigne 3 : Livres > 400 pages
print("\n=== LIVRES > 400 PAGES ===")
maBiblio.display_books_over_400_pages()

# Consigne 4 : Auteurs français
print("\n=== AUTEURS FRANÇAIS ===")
maBiblio.display_french_authors_books()

# Consigne 5 : Modification des auteurs < 1850
print("\n=== MODIFICATION AUTEURS ===")
maBiblio.update_old_books_author()

# Consigne 6 : Retour des livres avec 3 mots
print("\n=== RETOUR LIVRES 3 MOTS ===")
maBiblio.return_three_words_books()

# Consigne 7 : Total pages (méthode magique)
print(f"\n=== TOTAL PAGES (livres empruntés < 1900) : {len(maBiblio)} pages ===")

# Consigne 8 : Réaffichage après modifications
print("\n=== AFFICHAGE FINAL (APRÈS MODIFICATIONS) ===")
maBiblio.display_books_all()

# Consigne 9 : Sauvegarde
maBiblio.save_to_json("book_out.json")

print("\n" + "="*50)
print(maBiblio)  # état final