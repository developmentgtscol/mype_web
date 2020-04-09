from flask import Flask

from mype.view.ejemplo import vista_de_ejemplo

app = Flask(__name__)

@app.route('/')
def hello():
  ejemplo = vista_de_ejemplo()
  return ejemplo

# iniciador
if __name__ == '__main__':
   app.run(debug=True)

