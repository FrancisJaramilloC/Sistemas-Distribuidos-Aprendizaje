import time
import os


DIR_COMUNICACION = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'archivos_comunicacion')
os.makedirs(DIR_COMUNICACION, exist_ok=True)

ENTRADA_FILE = os.path.join(DIR_COMUNICACION, 'entrada_servidor.txt')
SALIDA_FILE = os.path.join(DIR_COMUNICACION, 'salida_servidor.txt')

def procesar_mensaje(mensaje):
    return mensaje.upper()[::-1]

def main():
    print(f"Servidor iniciado en'{ENTRADA_FILE}'...\n")
    
    #si no hay archivo se crea
    if not os.path.exists(ENTRADA_FILE):
        with open(ENTRADA_FILE, 'w', encoding='utf-8') as f:
            f.write('')
    
    ultimo_contenido = ""

    while True:
        try:
            #se lee el archivo de entrada
            with open(ENTRADA_FILE, 'r', encoding='utf-8') as f:
                contenido_actual = f.read().strip()
                
            #no procesar archivos vacios/no reprocesar el mismo mensaje
            if contenido_actual and contenido_actual != ultimo_contenido:
                print(f"Texto ingresado: '{contenido_actual}'")
                
                #procesa el mensaje
                resultado = procesar_mensaje(contenido_actual)
                
                #escribe la salida en el txt de salida
                with open(SALIDA_FILE, 'w', encoding='utf-8') as f:
                    f.write(resultado + '\n')
                print(f"Resultado escrito en '{SALIDA_FILE}': '{resultado}'\n")
                
                #actualiza el ultimo contenido procesado
                ultimo_contenido = contenido_actual
                
        except Exception as e:
            print(f"Error al leer/escribir archivos: {e}")
            
        #pausa antes de volver a revisar (para q no explote nada)
        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nServidor detenido")
