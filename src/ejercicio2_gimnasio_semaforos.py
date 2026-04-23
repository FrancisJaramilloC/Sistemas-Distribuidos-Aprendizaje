import threading
import logging
import time
import random

logging.basicConfig(level=logging.INFO, format='%(message)s') 

class MiSemaforo:
    #se crea el semaforo
    def __init__(self, valor):
        self.contador = valor
        self.cerrojo = threading.Lock()
        self.cola_espera = threading.Condition(self.cerrojo)
    
    #semaforo disminuye 1 (esperar)
    def esperar(self):
        self.cerrojo.acquire()
        while self.contador == 0:
            self.cola_espera.wait()
        self.contador -= 1
        self.cerrojo.release()

    #semaforo aumenta 1 (liberar)
    def senial(self):
        self.cerrojo.acquire()
        self.contador += 1
        self.cola_espera.notify()
        self.cerrojo.release()

#semaforo limitado a 3
semaforo = MiSemaforo(3)


resources_in_use = 0 
max_resources_in_use = 0 #variable que nunca superara a 3
monitoreo_cerrojo = threading.Lock() #monitorear la maquina


def atleta(id_atleta):
    global resources_in_use, max_resources_in_use
    semaforo.esperar() #espera a que un atleta libere la maquina
    with monitoreo_cerrojo: 
        resources_in_use += 1
        if resources_in_use > max_resources_in_use: 
            max_resources_in_use = resources_in_use
            
    logging.info(f"Atleta {id_atleta} usando máquina. (Máquinas en uso: {resources_in_use})")
    time.sleep(random.uniform(0.1, 0.5)) #espera aleatoria de uso
    
    with monitoreo_cerrojo: #se actualiza la variable
        resources_in_use -= 1
        
    semaforo.senial() #libera el semaforo
    logging.info(f"Atleta {id_atleta} liberó la máquina")

if __name__ == "__main__":
    N_ATLETAS = 10
    hilos = []
    
    for i in range(1, N_ATLETAS + 1):
        t = threading.Thread(target=atleta, args=(i,))
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()
    
    logging.info(f"Valor máximo de resources_in_use alcanzado: {max_resources_in_use}")
    assert max_resources_in_use <= 3, "El valor superó 3, el semáforo falló."
