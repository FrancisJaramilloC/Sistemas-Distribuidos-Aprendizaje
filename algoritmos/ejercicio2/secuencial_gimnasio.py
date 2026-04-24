import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')

N_ATLETAS = 10
TIEMPO_USO = 0.2

if __name__ == "__main__":
    inicio = time.time()
    for i in range(1, N_ATLETAS + 1):
        time.sleep(TIEMPO_USO)
        logging.info(f"Atleta {i} terminó")
    tiempo = time.time() - inicio
    logging.info(f"Tiempo: {tiempo:.4f}s")
