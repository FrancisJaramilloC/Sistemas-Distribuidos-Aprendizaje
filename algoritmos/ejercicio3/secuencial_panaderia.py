import logging
import time
import random

logging.basicConfig(level=logging.INFO, format='%(message)s')

CAPACIDAD = 10
TOTAL = 20

if __name__ == "__main__":
    inicio = time.time()
    vitrina = [None] * CAPACIDAD
    idx_insertar = 0
    idx_sacar = 0
    #primero hornea todos
    for i in range(1, TOTAL + 1):
        pan = f"Pan-{i}"
        vitrina[idx_insertar] = pan
        logging.info(f"[+] Panadero colocó {pan} en vitrina[{idx_insertar}]")
        idx_insertar = (idx_insertar + 1) % CAPACIDAD
        time.sleep(random.uniform(0.01, 0.05))
    #luego consume todos
    for i in range(1, TOTAL + 1):
        pan = f"Pan-{i}"
        logging.info(f"Cliente sacó y comió {pan} de vitrina[{idx_sacar}]")
        vitrina[idx_sacar] = None
        idx_sacar = (idx_sacar + 1) % CAPACIDAD
        time.sleep(random.uniform(0.05, 0.1))
    tiempo = time.time() - inicio
    logging.info(f"Total Horneados: {TOTAL} | Total Comprados: {TOTAL}")
    logging.info(f"Tiempo: {tiempo:.4f}s")
