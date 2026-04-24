import threading
import logging
import time
import random

logging.basicConfig(level=logging.INFO, format='%(message)s')

contador = 0 
N_TOTAL = 5 
mtx_barrera = threading.Lock() #mutex protege el acceso al contador
var_cond_barrera = threading.Condition(mtx_barrera) #donde los hilos esperan

hilos_fase1_terminada = 0 
verificacion_lock = threading.Lock()

def llegar_a_barrera(id_hilo):
    global contador
    
    mtx_barrera.acquire() #poner candado
    contador += 1
    
    if contador == N_TOTAL:
        var_cond_barrera.notify_all() #el ultimo hilo despierta a todos
    else:
        while contador < N_TOTAL:
            var_cond_barrera.wait() #los demas se duermen y sueltan el mutex
            
    mtx_barrera.release() #quitar candado al salir

def tarea_hilo(id_hilo):
    global hilos_fase1_terminada
    
    #fase 1
    logging.info(f"[+] Hilo {id_hilo} trabajando en Fase 1")
    time.sleep(random.uniform(0.1, 0.5))
    
    with verificacion_lock:
        hilos_fase1_terminada += 1
        
    logging.info(f"[-] Hilo {id_hilo} llega a la barrera y espera.")
    
    #llama a la barrera de sincronizacion
    llegar_a_barrera(id_hilo)
    
    #fase 2
    with verificacion_lock:
        assert hilos_fase1_terminada == N_TOTAL, "Error: Un hilo inició Fase 2 antes de tiempo."
        
    logging.info(f"[+] Hilo {id_hilo} trabajando en Fase 2")

if __name__ == "__main__":
    hilos = []
    
    #inicia hilos
    for i in range(1, N_TOTAL + 1):
        t = threading.Thread(target=tarea_hilo, args=(i,))
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()
        
    logging.info("Ningún hilo inició la fase 2 antes de que todos completaran la fase 1")
