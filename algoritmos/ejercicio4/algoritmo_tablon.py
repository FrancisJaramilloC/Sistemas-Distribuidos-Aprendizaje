import threading
import logging
import time
import random

logging.basicConfig(level=logging.INFO, format='%(message)s')

#semaforos y mutex
cant_lectores = 0 
mutex_lectores = threading.Lock() #protege el contador de lectores (q vaya de 1 en 1)
llave_escritura = threading.Semaphore(1) #semaforo para controlar el acceso al tablon
orden_llegada = threading.Semaphore(1) #semaforo para controlar el orden de llegada

lectores_activos = 0
escritores_activos = 0
verificacion_lock = threading.Lock()

def lector(id_lector):
    global cant_lectores, lectores_activos
    
    orden_llegada.acquire() #se pide permiso para entrar
    mutex_lectores.acquire() #se bloquea el contador de lectores
    cant_lectores += 1

    if cant_lectores == 1: #si es el primer lector pide permiso para entrar
        llave_escritura.acquire() 
    mutex_lectores.release()

    orden_llegada.release() #libera el semaforo
    
    #Lee el tablon 
    with verificacion_lock:
        lectores_activos += 1
        assert escritores_activos == 0, "Error: Hay un escritor modificando mientras se lee."
        
    logging.info(f"[+] Lector {id_lector} Leyendo. (Total leyendo juntos: {lectores_activos})")
    time.sleep(random.uniform(0.1, 0.3))
    
    with verificacion_lock:
        lectores_activos -= 1
    logging.info(f"[-] Lector {id_lector} se fue.")
    
    mutex_lectores.acquire() 
    cant_lectores -= 1
    if cant_lectores == 0: #si es el ultimo lector, libera el acceso al tablon
        llave_escritura.release() 
    mutex_lectores.release()

def escritor(id_escritor):
    global escritores_activos
    
    orden_llegada.acquire()  #bloquea nuevos lectores
    llave_escritura.acquire() #espera exclusividad en el tablon
    orden_llegada.release() #libera el semaforo
    
    #Escribir en el tablon 
    with verificacion_lock:
        escritores_activos += 1
        assert escritores_activos == 1, "Error: Varios escritores a la vez."
        assert lectores_activos == 0, "Error: Hay lectores leyendo mientras se escribe."
        
    logging.info(f"[+] Escritor {id_escritor} Escribiendo...")
    time.sleep(random.uniform(0.2, 0.5))
    
    with verificacion_lock:
        escritores_activos -= 1
    logging.info(f"[-] Escritor {id_escritor} terminó de escribir y liberó el tablón.")
    llave_escritura.release() #libera el tablon

if __name__ == "__main__":
    hilos = []
    
    inicio = time.time()
    #llegada de lectores
    for i in range(1, 4):
        t = threading.Thread(target=lector, args=(i,))
        hilos.append(t)
        t.start()
        
    time.sleep(0.05) 
    
    #llegada del escritor
    t = threading.Thread(target=escritor, args=(1,))
    hilos.append(t)
    t.start()
        
    #llegada de mas lectores
    for i in range(4, 8):
        t = threading.Thread(target=lector, args=(i,))
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()
    tiempo = time.time() - inicio
        
    logging.info("Validación Assert completada")
    logging.info("El log evidencia el patrón de acceso correcto")
    logging.info(f"Tiempo: {tiempo:.4f}s")

