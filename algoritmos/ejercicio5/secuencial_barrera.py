import logging
import time
import random

logging.basicConfig(level=logging.INFO, format='%(message)s')

N_TOTAL = 5

if __name__ == "__main__":
    inicio = time.time()
    #fase 1
    for i in range(1, N_TOTAL + 1):
        logging.info(f"[+] Hilo {i} trabajando en Fase 1")
        time.sleep(random.uniform(0.1, 0.5))
        logging.info(f"[-] Hilo {i} llega a la barrera y espera.")
    #fase 2
    for i in range(1, N_TOTAL + 1):
        logging.info(f"[+] Hilo {i} trabajando en Fase 2")
        time.sleep(random.uniform(0.1, 0.5))
    tiempo = time.time() - inicio
    logging.info(f"Tiempo: {tiempo:.4f}s")
