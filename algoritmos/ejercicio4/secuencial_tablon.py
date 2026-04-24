import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')

N_LECTORES = 7
N_ESCRITORES = 1
TIEMPO_LECTURA = 0.15
TIEMPO_ESCRITURA = 0.3

if __name__ == "__main__":
    inicio = time.time()
    for i in range(1, N_LECTORES + 1):
        time.sleep(TIEMPO_LECTURA)
        logging.info(f"Lector {i} leyó")
    for i in range(1, N_ESCRITORES + 1):
        time.sleep(TIEMPO_ESCRITURA)
        logging.info(f"Escritor {i} escribió")
    tiempo = time.time() - inicio
    logging.info(f"Tiempo: {tiempo:.4f}s")
