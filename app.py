from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    html_content = "<html><body><h1>Bem vindos!O Que Ver Hoje?</h1></body><span>Encontraremos aqui Diversos filtros e dicas do que ver hoje</span></html>"

    return html_content

if __name__ == '__main__':
    app.run()
