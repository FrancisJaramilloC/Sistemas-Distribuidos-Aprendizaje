from flask import Flask, render_template, Response
import subprocess
import os

app = Flask(__name__, template_folder='frontend')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream/<int:ejercicio>')
def stream_ejercicio(ejercicio):
    archivos = {
        1: 'ejercicio1_taquilla_mutex.py',
        2: 'ejercicio2_gimnasio_semaforos.py',
        3: 'ejercicio3_panaderia_productor_consumidor.py',
        4: 'ejercicio4_notas_escritor_lector.py',
        5: 'ejercicio5_encuentro_barrera.py'
    }
    
    if ejercicio not in archivos:
        return Response("data: Error: Ejercicio no encontrado\n\n", mimetype='text/event-stream')
        
    script_path = os.path.join('algoritmos', archivos[ejercicio])
    
    if not os.path.exists(script_path):
        return Response(f"data: Error: Archivo no encontrado: {script_path}\n\n", mimetype='text/event-stream')
    
    def generate():
        try:
            # -u obliga a python a imprimir en tiempo real sin guardar en buffer
            process = subprocess.Popen(
                ['python', '-u', script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            for line in iter(process.stdout.readline, ''):
                # El formato SSE envía prefijo "data: " y finaliza con "\n\n"
                yield f"data: {line}\n\n"
                
            process.stdout.close()
            process.wait()
            yield "data: [FIN_EJECUCION]\n\n"
        except Exception as e:
            yield f"data: Error interno al ejecutar: {str(e)}\n\n"
            
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
