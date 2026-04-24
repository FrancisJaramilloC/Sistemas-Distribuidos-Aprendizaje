# Sistemas Distribuidos - Simulador de Concurrencia

Este proyecto contiene ejercicios practicos de sincronizacion y concurrencia.

## Estructura del proyecto

```
algoritmos/
  ejercicio1/
    algoritmo_taquilla.py
    benchmark_taquilla.py
  ejercicio2/
    algoritmo_gimnasio.py
    benchmark_gimnasio.py
  ejercicio3/
    algoritmo_panaderia.py
    benchmark_panaderia.py
  ejercicio4/
    algoritmo_tablon.py
    benchmark_tablon.py
  ejercicio5/
    algoritmo_barrera.py
    benchmark_barrera.py
frontend/
  index.html
app.py
```

## Descripcion de los Algoritmos

### 1. La Taquilla (Mutex)
Usa un cerrojo para evitar sobreventa de boletos cuando varios clientes compran al mismo tiempo.

### 2. El Gimnasio (Semaforos)
Usa un semaforo para limitar el acceso a 3 maquinas. Los atletas que llegan esperan su turno.

### 3. La Panaderia (Productor-Consumidor)
Coordina un panadero y un cliente con un buffer circular. El panadero no hornea si la vitrina esta llena, el cliente no come si esta vacia.

### 4. Tablon de Notas (Lectores-Escritores)
Permite que varios estudiantes lean al mismo tiempo, pero solo un profesor puede escribir de forma exclusiva.

### 5. Sincronizacion (Barrera)
Obliga a todos los hilos a esperar en un punto comun antes de avanzar juntos a la siguiente fase.

---

## Como ejecutar los algoritmos

Cada ejercicio tiene dos archivos independientes. Desde la raiz del proyecto:

```bash
python algoritmos/ejercicio1/algoritmo_taquilla.py
python algoritmos/ejercicio1/benchmark_taquilla.py
```

Cambia el numero del ejercicio y el nombre para probar otro.

---

## Como ejecutar la interfaz web

### Paso 1: Preparar el entorno
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Paso 2: Iniciar el servidor
```bash
python app.py
```

### Paso 3: Abrir en el navegador
http://127.0.0.1:5000

Cada ejercicio tiene dos botones: Algoritmo y Benchmark.