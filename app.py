from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!doctype html>
        <html lang="es">
          <head>
            <meta charset="utf-8">
            <style>
              #imagen {
                display: none;
                width: 200px;
                height: auto;
              }
            </style>
          </head>
          <body>
            <h1>Hola mundo</h1>
            <button onclick="mostrarMensaje()">Mostrar Nombre y grupo</button>
            <p id="mensaje"></p>
            <img id="imagen" src="/static/imagen2.jpg" alt="Imagen de ejemplo">
            <script>
              function mostrarMensaje() {
                fetch('/mensaje')
                  .then(response => response.text())
                  .then(data => {
                    document.getElementById('mensaje').innerText = data;
                    document.getElementById('imagen').style.display = 'block';
                  });
              }
            </script>
          </body>
        </html>
    '''

@app.route('/mensaje')
def mensaje():
    return "Alumno: Aldo de Jesus Hernandez Celestino, Grupo 9°-B"

if __name__ == '__main__':
    app.run(debug=True)

