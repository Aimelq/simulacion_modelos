#Aimel Quijada
#C.I 30.729.553
import random

def main():
    apuesta_inicial = 5
    ganancia_acumulada = 0
    perdida_acumulada = 0
    epicas = []  # Lista para guardar las épicas (1 si gana, 0 si pierde)

    for ronda in range(1, 101):  # Límite de 100 iteraciones
        dado = random.randint(1, 6)
        if dado % 2 == 0:  # Número par
            ganancia_acumulada += apuesta_inicial * 2  # Ganancia duplicada
            epicas.append(1)
            print(f"Ronda {ronda}: ¡Ganaste! Ganancia: ${apuesta_inicial * 2}")
        else:  # Número impar
            perdida_acumulada += apuesta_inicial
            epicas.append(0)
            print(f"Ronda {ronda}: ¡Perdiste! Pérdida: ${apuesta_inicial}")

        if perdida_acumulada >= 100:
            print("Límite de pérdida alcanzado. El programa termina.")
            break
        elif ganancia_acumulada >= 500:
            print("Límite de ganancia alcanzado. El programa termina.")
            break
    else:
        print("Límite de iteraciones alcanzado. El programa termina.")

    total_rondas = len(epicas)
    rondas_ganadas = sum(epicas)
    rondas_perdidas = total_rondas - rondas_ganadas

    porcentaje_ganadas = (rondas_ganadas / total_rondas) * 100
    porcentaje_perdidas = (rondas_perdidas / total_rondas) * 100

    print(f"\nResumen:")
    print(f"Rondas ganadas: {rondas_ganadas} ({porcentaje_ganadas:.2f}%)")
    print(f"Rondas perdidas: {rondas_perdidas} ({porcentaje_perdidas:.2f}%)")

if __name__ == "__main__":
    main()
