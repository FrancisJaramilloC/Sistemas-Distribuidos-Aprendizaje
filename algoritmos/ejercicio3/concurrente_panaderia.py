import threading
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')

CAPACIDAD = 10
TOTAL = 20
TIEMPO_HORNEAR = 0.05
TIEMPO_COMER = 0.05

if __name__ == "__main__":
    espacios = threading.Semaphore(CAPACIDAD)
    panes = threading.Semaphore(0)
    mutex = threading.Lock()
    buf = [None] * CAPACIDAD
    idx = [0, 0]
    
    def panadero():
        for i in range(1, TOTAL + 1):
            time.sleep(TIEMPO_HORNEAR)
            espacios.acquire()
            with mutex:
                buf[idx[0]] = i
                idx[0] = (idx[0] + 1) % CAPACIDAD
            panes.release()
            logging.info(f"Horneó Pan-{i}")
    
    def cliente():
        for i in range(1, TOTAL + 1):
            panes.acquire()
            with mutex:
                buf[idx[1]] = None
                idx[1] = (idx[1] + 1) % CAPACIDAD
            espacios.release()
            logging.info(f"Comió Pan-{i}")
            time.sleep(TIEMPO_COMER)
    
    inicio = time.time()
    t1 = threading.Thread(target=panadero)
    t2 = threading.Thread(target=cliente)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    tiempo = time.time() - inicio
    logging.info(f"Tiempo: {tiempo:.4f}s")
