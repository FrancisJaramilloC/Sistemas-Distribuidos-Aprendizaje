import threading
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')

N_ATLETAS = 10
TIEMPO_USO = 0.2

if __name__ == "__main__":
    sem = threading.Semaphore(3)
    
    def atleta(id_a):
        sem.acquire()
        time.sleep(TIEMPO_USO)
        sem.release()
        logging.info(f"Atleta {id_a} terminó")
    
    inicio = time.time()
    hilos = []
    for i in range(1, N_ATLETAS + 1):
        t = threading.Thread(target=atleta, args=(i,))
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()
    tiempo = time.time() - inicio
    logging.info(f"Tiempo: {tiempo:.4f}s")
