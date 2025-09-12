# Ejemplo de inferencias con Modus Ponens
# Sistema experto de llantas (autos y rines)

# --- Base de reglas ---
# Auto -> Rin
auto_a_rin = {
    "Nissan Tsuru 2004": "14 pulgadas",
    "Toyota Corolla 2004": "15 pulgadas"
}

# Rin -> Llanta
rin_a_llanta = {
    "14 pulgadas": "185/65 R14",
    "15 pulgadas": "195/65 R15",
    "16 pulgadas": "205/55 R16"
}


# --- Modus Ponens ---
# Si P → Q y Q → R, entonces P → R
def modus_ponens(auto):
    print("\n=== Ejemplo Modus Ponens ===")
    print("Regla 1: Si auto = Nissan Tsuru 2004, entonces rin = 14 pulgadas.")
    print("Regla 2: Si rin = 14 pulgadas, entonces llanta = 185/65 R14.")
    print(f"Hecho: El auto es {auto}.")

    rin = auto_a_rin.get(auto)
    if rin:
        llanta = rin_a_llanta.get(rin)
        if llanta:
            print(f"Conclusión: Para el auto {auto}, el rin es {rin} y la llanta recomendada es {llanta}.")
        else:
            print(f"No tengo datos de llanta para rin {rin}.")
    else:
        print("No se puede aplicar Modus Ponens: el auto no coincide con ninguna regla.")



# --- Ejecución de ejemplos ---
modus_ponens("Nissan Tsuru 2004")          # Caso auto->rin->llanta


