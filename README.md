# Sistemas Distribuidos - Simulador de Concurrencia

Este proyecto contiene una serie de ejercicios practicos para comprender problemas clasicos de sincronizacion y concurrencia.

## Descripcion de los Algoritmos

### 1. La Taquilla (Mutex)
Simula la venta de boletos en una base de datos centralizada. Utiliza un cerrojo (Mutex) para asegurar que varios clientes no sobrevendan asientos al mismo tiempo, garantizando una suma exacta de ventas.

### 2. El Gimnasio (Semaforos)
Simula un gimnasio con maquinas limitadas. Utiliza un semaforo para controlar el acceso, permitiendo que un maximo de 3 atletas usen el recurso simultaneamente mientras el resto espera su turno de forma ordenada.

### 3. La Panaderia (Productor-Consumidor)
Implementa un sistema de buffer o almacenamiento. El panadero hornea pan solo si hay espacio en la vitrina, y el cliente toma pan solo si la vitrina no esta vacia, coordinando que ninguno trabaje con datos incorrectos.

### 4. Tablon de Notas (Lectores-Escritores)
Resuelve el problema de acceso a informacion compartida. Permite que varios estudiantes lean el tablon al mismo tiempo, pero requiere acceso totalmente exclusivo para el profesor cuando va a escribir. Usa un mecanismo de fila para evitar que el profesor espere para siempre.

### 5. Sincronizacion (Barrera)
Simula tareas que se dividen en fases. Utiliza una "barrera" para obligar a todos los procesos rápidos a detenerse y esperar hasta que el ultimo proceso termine la Fase 1. Cuando el ultimo llega, todos avanzan juntos a la Fase 2.

---

## Como ejecutar los algoritmos individualmente

Los algoritmos se encuentran en la carpeta `algoritmos`. No requieren instalaciones complejas.

Para ejecutar cualquiera de ellos y ver su salida directo en la consola, abre tu terminal en la raiz del proyecto y ejecuta el archivo con Python:

```bash
python algoritmos/ejercicio1_taquilla_mutex.py
```

Puedes cambiar el nombre del archivo para probar el ejercicio 2, 3, 4 o 5. 

---

## Como ejecutar la interfaz web (Flask)

El proyecto incluye un portal web para probar todos los algoritmos de manera visual.

### Paso 1: Activar el entorno virtual
Primero, debes preparar el entorno donde viven las dependencias del servidor. En la raiz del proyecto ejecuta:

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Paso 2: Encender el servidor
Con el entorno activado, inicia el programa principal de Flask:

```bash
python app.py
```

### Paso 3: Usar el simulador
Abre tu navegador de internet y entra a la siguiente direccion:
http://127.0.0.1:5000

Selecciona el ejercicio que desees en la pantalla y presiona ejecutar para ver los resultados en tiempo real.