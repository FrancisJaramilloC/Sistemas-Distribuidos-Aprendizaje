import threading
import logging
import time
import random

logging.basicConfig(level=logging.INFO, format='%(message)s') #logs del programa

#semaforos y Mutex
CAPACIDAD = 10
espacios_vacios = threading.Semaphore(CAPACIDAD) #semaforo de espacios disponibles
panes_listos = threading.Semaphore(0) #semaforo de panes listos
mutex_vitrina = threading.Lock() #mutex para la vitrina

# Buffer Circular
vitrina = [None] * CAPACIDAD
indice_insertar = 0
indice_sacar = 0

#verificar secuencia y completitud
TOTAL_A_PRODUCIR = 20
panes_horneados_historial = []
panes_comprados_historial = []

#panadero
def panadero():
    global indice_insertar
    for i in range(1, TOTAL_A_PRODUCIR + 1):
        pan = f"Pan-{i}" # Hornear pan
        espacios_vacios.acquire() #esperar

        with mutex_vitrina: #mutex (bloquear/desbloquear)
            vitrina[indice_insertar] = pan 
            panes_horneados_historial.append(pan) 
            logging.info(f"[+] Panadero colocó {pan} en vitrina[{indice_insertar}]") 
            indice_insertar = (indice_insertar + 1) % CAPACIDAD 
            
        panes_listos.release() #libera los panes en la vitrina
        time.sleep(random.uniform(0.01, 0.05))

def cliente():
    global indice_sacar
    for _ in range(TOTAL_A_PRODUCIR):
        panes_listos.acquire() #esperar panes_listos
        
        with mutex_vitrina: #mutex (bloquear/desbloquear)
            pan = vitrina[indice_sacar] 
            vitrina[indice_sacar] = None 
            panes_comprados_historial.append(pan)
            logging.info(f"Cliente sacó y comió {pan} de vitrina[{indice_sacar}]")
            indice_sacar = (indice_sacar + 1) % CAPACIDAD 
            
        espacios_vacios.release() #incrementar espacios_vacios
        time.sleep(random.uniform(0.05, 0.1)) # El cliente come más lento


if __name__ == "__main__":
    
    t_panadero = threading.Thread(target=panadero)
    t_cliente = threading.Thread(target=cliente)

    t_panadero.start()
    t_cliente.start()

    t_panadero.join()
    t_cliente.join()
    
    es_secuencia_correcta = (panes_horneados_historial == panes_comprados_historial)
    logging.info(f"Total Horneados: {len(panes_horneados_historial)} | Total Comprados: {len(panes_comprados_historial)}")
    logging.info(f"Los panes fueron consumidos en orden?: {es_secuencia_correcta}")
    assert es_secuencia_correcta, "Error de completitud o secuencia."
