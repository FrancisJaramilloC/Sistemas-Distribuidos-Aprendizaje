import logging
import time
import random

logging.basicConfig(level=logging.INFO, format='%(message)s')

N_LECTORES = 7
N_ESCRITORES = 1
TIEMPO_LECTURA = 0.15
TIEMPO_ESCRITURA = 0.3

if __name__ == "__main__":
    inicio = time.time()
    #lectores 1-3
    for i in range(1, 4):
        logging.info(f"[+] Lector {i} Leyendo. (Total leyendo juntos: 1)")
        time.sleep(random.uniform(0.1, 0.3))
        logging.info(f"[-] Lector {i} se fue.")
    #escritor
    for i in range(1, N_ESCRITORES + 1):
        logging.info(f"[+] Escritor {i} Escribiendo...")
        time.sleep(random.uniform(0.2, 0.5))
        logging.info(f"[-] Escritor {i} terminó de escribir y liberó el tablón.")
    #lectores 4-7
    for i in range(4, N_LECTORES + 1):
        logging.info(f"[+] Lector {i} Leyendo. (Total leyendo juntos: 1)")
        time.sleep(random.uniform(0.1, 0.3))
        logging.info(f"[-] Lector {i} se fue.")
    tiempo = time.time() - inicio
    logging.info(f"Tiempo: {tiempo:.4f}s")
