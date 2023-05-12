from flask import Flask, jsonify, request
import ssl, json

app = Flask(__name__)

#Post teste
@app.route("/teste", methods=['POST', 'GET'])
def imprimir():
    if request.method == 'GET':
        print('Recebi um GET')
        return jsonify({"status": 200})
    
    if request.method == "POST":
        response = request.get_json()
        print(response)
        return jsonify({"status": 200})

#Post para o blip
@app.route("/", methods=['POST'])
def imprimirChat():
    imprime = print(request.json)
    data = request.get_json()
    with open('database_pymongo/history.json', 'a') as outfile:
        outfile.write('\n')
        json.dump(data, outfile)
    return 'OK'

#Post para futuros filtros
@app.route('/filtro', methods=['POST'])
def webhook():
    data = request.get_json()
    return jsonify({'response': 'Webhook recebido com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)

    