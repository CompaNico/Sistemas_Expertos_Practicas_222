# Modulo de Aprendizaje Sistema experto en llantas
# sistema_experto_llantas.py

# Base inicial de conocimiento
autos = {
    "Nissan Tsuru 2004": "Original 14 pulgadas",
    "Toyota Corolla 2004": "Original 15 pulgadas",
    "Honda Civic 2004": "Original 15 pulgadas",
    "Ford Focus 2004": "Original 16 pulgadas",
    "Chevrolet Astra 2004": "Original 15 pulgadas"
}

rines = [
    "Original de agencia",
    "Enkei RPF1 16 pulgadas",
    "BBS SR 17 pulgadas",
    "OZ Racing Ultraleggera 16 pulgadas",
    "Konig Hypergram 17 pulgadas",
    "American Racing VN507 16 pulgadas"
]

# Recomendaciones simples de llantas
recomendaciones = {
    "14 pulgadas": "Llanta 185/65 R14, ideal para ciudad y economía",
    "15 pulgadas": "Llanta 195/65 R15, equilibrio entre confort y agarre",
    "16 pulgadas": "Llanta 205/55 R16, mayor estabilidad",
    "17 pulgadas": "Llanta 215/45 R17, estilo deportivo y buen desempeño"
}

# Bienvenida
print("Bienvenido al Sistema Experto en Llantas")
print("Estoy aquí para recomendarte llantas según tu auto y rines.")
print("Por ahora trabajo con autos del 2004 y algunas marcas de rines.\n")

def recomendar_llanta(auto, rin):
    # Si el auto está en la base
    if auto in autos:
        medida_auto = autos[auto].split()[-2]  # ejemplo: "14 pulgadas"
    else:
        print(f"No conozco el auto '{auto}'.")
        nuevo = input("¿Quieres agregarlo a la base de datos? (s/n): ")
        if nuevo.lower() == "s":
            medida = input("Ingresa la medida original de rines (ej. '15 pulgadas'): ")
            autos[auto] = "Original " + medida
            medida_auto = medida
        else:
            return "No puedo recomendar sin datos del auto."

    # Si el rin está en la base
    if rin in rines:
        medida_rin = rin.split()[-2]  # tomar la medida, ej: "16"
        medida_rin += " pulgadas"
    else:
        print(f"No conozco el rin '{rin}'.")
        nuevo = input("¿Quieres agregarlo a la base de datos? (s/n): ")
        if nuevo.lower() == "s":
            medida_rin = input("Ingresa la medida del rin (ej. '17 pulgadas'): ")
            rines.append(rin + " " + medida_rin)
        else:
            return "No puedo recomendar sin datos del rin."

    # Decidir recomendación
    medida_final = medida_rin if medida_rin in recomendaciones else medida_auto
    return recomendaciones.get(medida_final, "No tengo recomendación para esa medida.")

# Flujo principal
auto_usuario = input("Ingresa tu auto (ejemplo: 'Nissan Tsuru 2004'): ")
rin_usuario = input("Ingresa el rin que usas (ejemplo: 'Enkei RPF1 16 pulgadas'): ")

print("\n--- RECOMENDACIÓN ---")
print(recomendar_llanta(auto_usuario, rin_usuario))
