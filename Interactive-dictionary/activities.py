from dictionary import Dictionary
from utilities import get_total, nth_letter_word

def main():
    print("=== Proyecto: Gestión de Diccionario, Precios y Creación de Palabras ===")

    # Parte 1: Diccionario de palabras
    print("\n--- Parte 1: Diccionario ---")
    dictionary = Dictionary()
    dictionary.newentry("Apple", "A fruit that grows on trees")
    dictionary.newentry("Python", "A programming language")
    print(f"Definición de 'Apple': {dictionary.look('Apple')}")
    print(f"Definición de 'Banana': {dictionary.look('Banana')}")

    # Parte 2: Cálculo de costos
    print("\n--- Parte 2: Cálculo de Costos ---")
    costs = {"socks": 5, "shoes": 60, "sweater": 30}
    purchased_items = ["socks", "shoes"]
    tax_rate = 0.09
    total_cost = get_total(costs, purchased_items, tax_rate)
    print(f"Productos comprados: {purchased_items}")
    print(f"Costo total con impuesto (9%): ${total_cost}")

    # Parte 3: Creación de palabras
    print("\n--- Parte 3: Creación de Palabras ---")
    words = ["yoda", "best", "has"]
    new_word = nth_letter_word(words)
    print(f"Lista de palabras: {words}")
    print(f"Palabra generada: {new_word}")

if __name__ == "__main__":
    main()