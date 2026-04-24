import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')

N_TOTAL = 5
TIEMPO_FASE = 0.2

if __name__ == "__main__":
    inicio = time.time()
    for i in range(1, N_TOTAL + 1):
        time.sleep(TIEMPO_FASE)
        logging.info(f"Hilo {i} completó Fase 1")
    for i in range(1, N_TOTAL + 1):
        time.sleep(TIEMPO_FASE)
        logging.info(f"Hilo {i} completó Fase 2")
    tiempo = time.time() - inicio
    logging.info(f"Tiempo: {tiempo:.4f}s")
