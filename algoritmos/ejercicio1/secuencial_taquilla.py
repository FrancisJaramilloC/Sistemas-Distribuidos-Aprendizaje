import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')

N_HILOS = 5
M_VENTAS = 1_000_000
TOTAL = N_HILOS * M_VENTAS

if __name__ == "__main__":
    inicio = time.time()
    for iteracion in range(1, 11):
        contador = 0
        for _ in range(TOTAL):
            contador += 1
        logging.info("Iteración %d - Ventas Totales: %d", iteracion, contador)
    tiempo = time.time() - inicio
    logging.info(f"Tiempo: {tiempo:.4f}s")
