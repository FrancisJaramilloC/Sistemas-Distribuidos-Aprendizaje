from flask import Flask, render_template, Response
import subprocess
import os

app = Flask(__name__, template_folder='frontend')

ARCHIVOS = {
    1: {'nombre': 'taquilla', 'carpeta': 'ejercicio1'},
    2: {'nombre': 'gimnasio', 'carpeta': 'ejercicio2'},
    3: {'nombre': 'panaderia', 'carpeta': 'ejercicio3'},
    4: {'nombre': 'tablon', 'carpeta': 'ejercicio4'},
    5: {'nombre': 'barrera', 'carpeta': 'ejercicio5'},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream/<int:ejercicio>/<tipo>')
def stream_ejercicio(ejercicio, tipo):
    if ejercicio not in ARCHIVOS or tipo not in ('algoritmo', 'secuencial'):
        return Response("data: Error: Ruta no válida\n\n", mimetype='text/event-stream')
    
    info = ARCHIVOS[ejercicio]
    archivo = f"{tipo}_{info['nombre']}.py"
    script_path = os.path.join('algoritmos', info['carpeta'], archivo)
    
    if not os.path.exists(script_path):
        return Response(f"data: Error: Archivo no encontrado: {script_path}\n\n", mimetype='text/event-stream')
    
    def generate():
        try:
            process = subprocess.Popen(
                ['python', '-u', script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            for line in iter(process.stdout.readline, ''):
                yield f"data: {line}\n\n"
                
            process.stdout.close()
            process.wait()
            yield "data: [FIN]\n\n"
        except Exception as e:
            yield f"data: Error: {str(e)}\n\n"
            
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
