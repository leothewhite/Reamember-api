from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)


dictionary_key = open('./key.txt', 'r').read()


@app.route('/api/reamember/get-word', methods=['POST'])
def get_word():
    print(request)

    word = request.get_json()['word']


    response = requests.request(url=f'https://stdict.korean.go.kr/api/search.do?certkey_no=7181&key={dictionary_key}&q={word}&req_type=json', method='get')

    print(response.text)

    return jsonify({
        'res': response.text
    })

app.run(host='0.0.0.0', port=2048, debug=True)