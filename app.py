from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/notifyMe', methods=['GET'])
def hello_world():
    json_content = {"message": "Bem-vindo",
                     "content":"Utilize o O Que Ver Agora?"    }
    return jsonify(json_content)

if __name__ == '__main__':
    app.run()

#comentario em python
"""
comentario de um bloco em python
"""