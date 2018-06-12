from flask import Flask, request
from flask_cors import CORS, cross_origin
import ujson as json
import utils

app = Flask(__name__)
CORS(app)

@app.route('/getEmbeddings',methods=['POST'])
def getEmbeddings():
	data = request.data
	if isinstance(data, str):
		data = json.loads(request.data)
	ret_obj = []
	for idx, d in enumerate(data):
		sent_key = 'S' + str(idx+1)
		l_key = 'L' + str(idx+1)
		sent = d[sent_key]
		lang = d[l_key]
		ret_obj.append({sent_key + '_embeddings':utils.fetch_vectors(lang, sent)})
	print(ret_obj)
	return json.dumps(ret_obj)

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=8080, debug = True)
