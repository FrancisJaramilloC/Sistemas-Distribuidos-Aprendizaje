import threading
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')

N_HILOS = 5
M_VENTAS = 1_000_000
boletos_vendidos = 0
mutex = threading.Lock()

def ejecutar_venta():
    global boletos_vendidos
    for _ in range(M_VENTAS):
        with mutex:
            boletos_vendidos += 1

if __name__ == "__main__":
    inicio = time.time()
    for iteracion in range(1, 11):
        boletos_vendidos = 0
        hilos = []
        for _ in range(N_HILOS):
            t = threading.Thread(target=ejecutar_venta)
            hilos.append(t)
            t.start()
        for t in hilos:
            t.join()
        logging.info("Iteración %d - Ventas Totales: %d", iteracion, boletos_vendidos)
    tiempo = time.time() - inicio
    logging.info(f"Tiempo: {tiempo:.4f}s")
