import threading
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')

N_TOTAL = 5
TIEMPO_FASE = 0.2

if __name__ == "__main__":
    contador = [0]
    mtx = threading.Lock()
    cond = threading.Condition(mtx)
    
    def tarea(id_h):
        time.sleep(TIEMPO_FASE) #fase 1
        logging.info(f"Hilo {id_h} completó Fase 1")
        mtx.acquire()
        contador[0] += 1
        if contador[0] == N_TOTAL:
            cond.notify_all()
        else:
            while contador[0] < N_TOTAL:
                cond.wait()
        mtx.release()
        time.sleep(TIEMPO_FASE) #fase 2
        logging.info(f"Hilo {id_h} completó Fase 2")
    
    inicio = time.time()
    hilos = []
    for i in range(1, N_TOTAL + 1):
        t = threading.Thread(target=tarea, args=(i,))
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()
    tiempo = time.time() - inicio
    logging.info(f"Tiempo: {tiempo:.4f}s")
