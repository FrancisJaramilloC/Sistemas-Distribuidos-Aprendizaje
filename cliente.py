import time
import os

DIR_COMUNICACION = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'archivos_comunicacion')
os.makedirs(DIR_COMUNICACION, exist_ok=True)

ENTRADA_FILE = os.path.join(DIR_COMUNICACION, 'entrada_servidor.txt')
SALIDA_FILE = os.path.join(DIR_COMUNICACION, 'salida_servidor.txt')

def main():
    print("Cliente Iniciado ")

    while True:
        try:
            #solicita un mensaje 
            mensaje = input("Ingrese un mensaje: ")

            #agarra ultima modificacion para saber si hubo algun cambio en salida txt
            ultima_modificacion = os.path.getmtime(SALIDA_FILE) if os.path.exists(SALIDA_FILE) else 0

            with open(ENTRADA_FILE, 'w', encoding='utf-8') as f:
                f.write(mensaje)
            print("Mensaje cargado en la entrada")
            
            #espera 3 segundos (puse q el servidor revisa cada 2 segundos porq sino peta)
            time.sleep(3)
            
            #lee la respuesta 
            modificacion_actual = os.path.getmtime(SALIDA_FILE) if os.path.exists(SALIDA_FILE) else 0

            if modificacion_actual > ultima_modificacion:
                with open(SALIDA_FILE, 'r', encoding='utf-8') as f:
                    respuesta = f.read().strip()
                print(f"Respuesta del servidor: {respuesta}\n")
            else:
                print("El servidor no ha respondido, corre el servidor\n")

        except Exception as e:
            print(f"Ocurrió un error en el cliente: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCliente cerrado.")
