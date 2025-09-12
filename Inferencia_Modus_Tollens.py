# Ejemplo de inferencias Modus Tollens
#Sistema experto de llantas (autos y rines)


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


# --- Modus Tollens ---
# Si R → Q, y Q es falso, entonces R es falso (invirtiendo razonamiento llanta -> rin -> auto)
def modus_tollens(llanta_observada, rin_observado):
    print("\n=== Ejemplo Modus Tollens ===")
    print("Regla: Si llanta = 185/65 R14, entonces rin = 14 pulgadas.")
    print(f"Hecho: La llanta observada es {llanta_observada}, pero el rin observado es {rin_observado}.")

    rin_esperado = None
    for rin, llanta in rin_a_llanta.items():
        if llanta == llanta_observada:
            rin_esperado = rin
            break

    if rin_esperado and rin_observado != rin_esperado:
        # Buscamos qué auto tenía ese rin esperado
        autos_relacionados = [a for a, r in auto_a_rin.items() if r == rin_esperado]
        print(f"Conclusión: El rin esperado era {rin_esperado}, pero como no coincide, el auto no es {', '.join(autos_relacionados)}.")
    else:
        print("No se puede aplicar Modus Tollens: no hay contradicción con la regla.")

#----------Ejecucion del ejemplo--------------------------
modus_tollens("185/65 R14", "16 pulgadas") # Caso llanta->rin->auto