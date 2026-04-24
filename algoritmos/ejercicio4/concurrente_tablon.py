import threading
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')

N_LECTORES = 7
N_ESCRITORES = 1
TIEMPO_LECTURA = 0.15
TIEMPO_ESCRITURA = 0.3

if __name__ == "__main__":
    llave = threading.Semaphore(1)
    mutex = threading.Lock()
    cant = [0]
    
    def lector(id_l):
        mutex.acquire()
        cant[0] += 1
        if cant[0] == 1:
            llave.acquire()
        mutex.release()
        time.sleep(TIEMPO_LECTURA)
        logging.info(f"Lector {id_l} leyó")
        mutex.acquire()
        cant[0] -= 1
        if cant[0] == 0:
            llave.release()
        mutex.release()
    
    def escritor(id_e):
        llave.acquire()
        time.sleep(TIEMPO_ESCRITURA)
        logging.info(f"Escritor {id_e} escribió")
        llave.release()
    
    inicio = time.time()
    hilos = []
    for i in range(1, N_LECTORES + 1):
        t = threading.Thread(target=lector, args=(i,))
        hilos.append(t)
        t.start()
    for i in range(1, N_ESCRITORES + 1):
        t = threading.Thread(target=escritor, args=(i,))
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()
    tiempo = time.time() - inicio
    logging.info(f"Tiempo: {tiempo:.4f}s")
