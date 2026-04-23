import threading
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s') 

boletos_vendidos = 0 #boleto iniciado en 0
#NxM = 5 000 000
N_HILOS = 5
M_VENTAS = 1_000_000
mutex = threading.Lock()

def ejecutar_venta():
    global boletos_vendidos
    for _ in range(M_VENTAS):
        with mutex:
            boletos_vendidos += 1

if __name__ == "__main__":
    for iteracion in range(1, 11): #10 iteraciones sin variacion
        boletos_vendidos = 0
        hilos = []
        
        for _ in range(N_HILOS):
            t = threading.Thread(target=ejecutar_venta)
            hilos.append(t)
            t.start()

        for t in hilos:
            t.join()

        logging.info("Iteración %d - Ventas Totales: %d", iteracion, boletos_vendidos)
