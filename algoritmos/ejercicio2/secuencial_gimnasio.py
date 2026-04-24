import logging
import time
import random

logging.basicConfig(level=logging.INFO, format='%(message)s')

N_ATLETAS = 10
CAPACIDAD_MAQUINAS = 3

if __name__ == "__main__":
    inicio = time.time()
    for i in range(1, N_ATLETAS + 1):
        logging.info(f"Atleta {i} usando máquina. (Máquinas en uso: 1)")
        time.sleep(random.uniform(0.1, 0.5))
        logging.info(f"Atleta {i} liberó la máquina")
    tiempo = time.time() - inicio
    logging.info(f"Tiempo: {tiempo:.4f}s")
