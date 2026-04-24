import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')

TOTAL = 20
TIEMPO_HORNEAR = 0.05
TIEMPO_COMER = 0.05

if __name__ == "__main__":
    inicio = time.time()
    vitrina = []
    for i in range(1, TOTAL + 1):
        time.sleep(TIEMPO_HORNEAR)
        vitrina.append(f"Pan-{i}")
        logging.info(f"Horneó Pan-{i}")
    for i in range(TOTAL):
        time.sleep(TIEMPO_COMER)
        logging.info(f"Comió {vitrina.pop(0)}")
    tiempo = time.time() - inicio
    logging.info(f"Tiempo: {tiempo:.4f}s")
